package cmd

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"

	"github.com/spf13/cobra"
)

var auditCmd = &cobra.Command{
	Use:   "audit [target_path]",
	Short: "Runs the Forma Critic Engine to score UI files",
	Long:  `Audits frontend code (HTML/React/Vue) against cognitive heuristics, WCAG accessibility, and visual consistency rules.`,
	Args:  cobra.ExactArgs(1),
	RunE: func(cmd *cobra.Command, args []string) error {
		targetPath := args[0]

		exePath, err := os.Executable()
		if err != nil {
			return err
		}

		baseDir := filepath.Dir(filepath.Dir(exePath))
		scriptPath := filepath.Join(baseDir, "src", "scripts", "critic.py")

		if _, err := os.Stat(scriptPath); os.IsNotExist(err) {
			scriptPath = filepath.Join(filepath.Dir(exePath), "src", "scripts", "critic.py")
		}

		out, err := exec.Command("python", scriptPath, targetPath).CombinedOutput()
		if err != nil {
			out, err = exec.Command("python3", scriptPath, targetPath).CombinedOutput()
		}

		if err != nil {
			// If Python exits with 1 (which critic.py might do on errors), we still want to show the output.
			if string(out) == "" {
				return fmt.Errorf("engine error: %v\nPath used: %s", err, scriptPath)
			}
		}

		fmt.Println(string(out))
		return nil
	},
}

func init() {
	rootCmd.AddCommand(auditCmd)
}
