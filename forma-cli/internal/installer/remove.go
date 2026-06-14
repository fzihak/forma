package installer

import (
	"fmt"
	"os"
	"path/filepath"
)

// Remove cleanly uninstalls Forma agents from all supported IDE directories in the current project
func Remove() error {
	fmt.Println("🧹 Scanning repository for Forma installations...")
	
	removedCount := 0

	for _, p := range Platforms {
		if p.SkillDir != "" {
			// Ensure we are only deleting the isolated /forma directory or specific copilot config
			targetPath := p.SkillDir
			
			// If it's a file configuration like Copilot, delete the file if it exists
			if p.ConfigFile != "" {
				targetPath = p.ConfigFile
			}

			if _, err := os.Stat(targetPath); !os.IsNotExist(err) {
				// Only delete if it specifically targets the 'forma' namespace or the specific injected file
				err := os.RemoveAll(targetPath)
				if err != nil {
					fmt.Printf("⚠️  Warning: Could not remove %s: %v\n", targetPath, err)
				} else {
					fmt.Printf("🗑️  Removed: %s\n", targetPath)
					removedCount++
				}
			}
		}

		// Also check global installation paths if applicable
		if p.GlobalDir != "" {
			homeDir, err := os.UserHomeDir()
			if err == nil {
				// Replace ~ with home dir
				globalPath := filepath.Join(homeDir, p.GlobalDir[2:])
				if _, err := os.Stat(globalPath); !os.IsNotExist(err) {
					err := os.RemoveAll(globalPath)
					if err == nil {
						fmt.Printf("🗑️  Removed (Global): %s\n", globalPath)
						removedCount++
					}
				}
			}
		}
	}

	if removedCount > 0 {
		fmt.Printf("\n✅ Successfully purged Forma from %d locations.\n", removedCount)
		fmt.Println("To completely remove the CLI wrapper, run: npm uninstall -g forma-cli")
	} else {
		fmt.Println("ℹ️  No Forma installations found in this repository.")
	}

	return nil
}
