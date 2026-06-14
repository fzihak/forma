package cmd

import (
	"github.com/fzihak/forma/internal/diagnostic"
	"github.com/fzihak/forma/internal/updater"
	"github.com/spf13/cobra"
)

var doctorCmd = &cobra.Command{
	Use:   "doctor",
	Short: "Diagnoses the local environment for Forma compatibility",
	Long:  `Scans for Python versions, IDE directory permissions, and internal bundle integrity to ensure the mathematical AI engines will run flawlessly.`,
	Run: func(cmd *cobra.Command, args []string) {
		updater.CheckForUpdates()
		diagnostic.RunDiagnostics()
	},
}

func init() {
	rootCmd.AddCommand(doctorCmd)
}
