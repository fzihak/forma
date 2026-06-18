package cmd

import (
	"fmt"
	"github.com/charmbracelet/huh"
	"github.com/fzihak/forma/internal/installer"
	"github.com/spf13/cobra"
)

var (
	aiPlatform    string
	globalInstall bool
	offline       bool
)

var initCmd = &cobra.Command{
	Use:   "init",
	Short: "Install Forma skill into your project",
	RunE: func(cmd *cobra.Command, args []string) error {
		platform := aiPlatform

		if platform == "" {
			detected, err := installer.DetectPlatform()
			if err == nil && detected != "" {
				platform = detected
				fmt.Printf("✓ Auto-detected %s environment.\n", detected)
			} else {
				// Interactive UI
				err := huh.NewSelect[string]().
					Title("Choose your AI coding assistant:").
					Options(
						huh.NewOption("Claude Code", "claude"),
						huh.NewOption("Cursor", "cursor"),
						huh.NewOption("Windsurf", "windsurf"),
						huh.NewOption("GitHub Copilot", "copilot"),
						huh.NewOption("Install to All", "all"),
					).
					Value(&platform).
					Run()

				if err != nil {
					return fmt.Errorf("setup cancelled")
				}
			}
		}

		cfg := installer.Config{
			Platform: platform,
			Global:   globalInstall,
			Offline:  offline,
		}

		return installer.Install(cfg)
	},
}

func init() {
	initCmd.Flags().StringVar(&aiPlatform, "ai", "", "Target AI assistant (claude, cursor, windsurf, copilot, continue, all)")
	initCmd.Flags().BoolVar(&globalInstall, "global", false, "Install globally")
	initCmd.Flags().BoolVar(&offline, "offline", false, "Use bundled assets, skip GitHub check")
	rootCmd.AddCommand(initCmd)
}
