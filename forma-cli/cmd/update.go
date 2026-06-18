package cmd

import (
	"fmt"
	"os/exec"
	"github.com/fzihak/forma/internal/updater"
	"github.com/spf13/cobra"
)

var updateCmd = &cobra.Command{
	Use:   "update",
	Short: "Update Forma to the latest version",
	Long:  `Checks for the latest version of Forma and installs it globally.`,
	RunE: func(cmd *cobra.Command, args []string) error {
		fmt.Println("🔄 Checking for the latest Forma updates...")

		latest, err := updater.GetLatestVersion()
		if err != nil {
			return fmt.Errorf("could not check for updates. Make sure you have an internet connection")
		}

		if latest == "" || latest == updater.CurrentVersion {
			fmt.Printf("✨ You are already on the latest version of Forma (%s)!\n", updater.CurrentVersion)
			return nil
		}

		fmt.Printf("🚀 Updating Forma from %s to %s...\n", updater.CurrentVersion, latest)

		out, err := exec.Command("npm", "update", "-g", "forma-cli").CombinedOutput()
		if err != nil {
			return fmt.Errorf("failed to update via npm. Error: %s\nTry updating manually from GitHub.", string(out))
		}

		fmt.Println("✅ Forma has been successfully updated!")
		return nil
	},
}

func init() {
	rootCmd.AddCommand(updateCmd)
}
