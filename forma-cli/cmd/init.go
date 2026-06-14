package cmd

import (
    "github.com/fzihak/forma/internal/installer"
    "github.com/spf13/cobra"
)

var (
    aiPlatform string
    globalInstall bool
    offline bool
)

var initCmd = &cobra.Command{
    Use:   "init",
    Short: "Install Forma skill into your project",
    RunE: func(cmd *cobra.Command, args []string) error {
        platform := aiPlatform

        if platform == "" {
            detected, err := installer.DetectPlatform()
            if err != nil {
                return err
            }
            platform = detected
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
