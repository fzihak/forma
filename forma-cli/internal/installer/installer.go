package installer

import (
    "fmt"
    "io/fs"
    "os"
    "os/exec"
    "path/filepath"
    "strings"

    "github.com/fzihak/forma/internal/assets"
)

type Config struct {
    Platform string
    Global   bool
    Offline  bool
}

func expandHome(path string) string {
    if strings.HasPrefix(path, "~/") {
        home, _ := os.UserHomeDir()
        return filepath.Join(home, path[2:])
    }
    return path
}

func Install(cfg Config) error {
    if cfg.Platform == "all" {
        for name := range Platforms {
            if err := installSingle(name, cfg); err != nil {
                fmt.Printf("  ✗ %s: %v\n", name, err)
            }
        }
        return nil
    }
    return installSingle(cfg.Platform, cfg)
}

func installSingle(platformName string, cfg Config) error {
    platform, ok := Platforms[platformName]
    if !ok {
        return fmt.Errorf("unknown platform: %s", platformName)
    }

    targetDir := platform.SkillDir
    if cfg.Global && platform.GlobalDir != "" {
        targetDir = expandHome(platform.GlobalDir)
    }

    fmt.Printf("Installing Forma for %s...\n", platform.Name)

    err := fs.WalkDir(assets.SkillFiles, "files", func(path string, d fs.DirEntry, err error) error {
        if err != nil {
            return err
        }

        relPath, _ := filepath.Rel("files", path)
        if relPath == "." {
            return nil
        }
        
        destPath := filepath.Join(targetDir, relPath)

        if d.IsDir() {
            return os.MkdirAll(destPath, 0755)
        }

        data, err := assets.SkillFiles.ReadFile(path)
        if err != nil {
            return err
        }
        
        // Ensure parent directory exists for file
        os.MkdirAll(filepath.Dir(destPath), 0755)
        return os.WriteFile(destPath, data, 0644)
    })

    if err != nil {
        return err
    }

	// Auto-install python dependencies
	fmt.Println("Installing Python dependencies...")
	exePath, _ := os.Executable()
	baseDir := filepath.Dir(filepath.Dir(exePath))
	reqPath := filepath.Join(baseDir, "src", "scripts", "requirements.txt")
	
	if _, err := os.Stat(reqPath); os.IsNotExist(err) {
		reqPath = filepath.Join(filepath.Dir(exePath), "src", "scripts", "requirements.txt")
	}

	cmd := exec.Command("python", "-m", "pip", "install", "-r", reqPath)
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	if err := cmd.Run(); err != nil {
		// Fallback to python3
		cmd3 := exec.Command("python3", "-m", "pip", "install", "-r", reqPath)
		cmd3.Stdout = os.Stdout
		cmd3.Stderr = os.Stderr
		if err3 := cmd3.Run(); err3 != nil {
			fmt.Printf("  ⚠️ Could not auto-install dependencies. Please run manually: pip install -r %s\n", reqPath)
		}
	}

    fmt.Printf("  ✓ Installed to %s\n", targetDir)
    return nil
}
