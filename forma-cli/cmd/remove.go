package cmd

import (
	"github.com/fzihak/forma/internal/installer"
	"github.com/spf13/cobra"
)

var removeCmd = &cobra.Command{
	Use:     "remove",
	Aliases: []string{"uninstall"},
	Short:   "Safely uninstall Forma agents from your project",
	Long:    `Scans the repository for all supported AI IDE directories and cleanly deletes the embedded Forma agents without touching your project files.`,
	RunE: func(cmd *cobra.Command, args []string) error {
		return installer.Remove()
	},
}

func init() {
	rootCmd.AddCommand(removeCmd)
}
