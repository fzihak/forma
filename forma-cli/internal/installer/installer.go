package installer

import (
    "fmt"
    "io/fs"
    "os"
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

    fmt.Printf("  ✓ Installed to %s\n", targetDir)
    return nil
}
