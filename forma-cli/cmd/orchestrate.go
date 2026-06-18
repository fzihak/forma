package cmd

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strings"

	"github.com/spf13/cobra"
)

var orchestrateCmd = &cobra.Command{
	Use:   "orchestrate [prompt]",
	Short: "Interacts with the Python intelligence engine to generate a UX mandate",
	Args:  cobra.ExactArgs(1),
	RunE: func(cmd *cobra.Command, args []string) error {
		prompt := args[0]
		
		fmt.Printf("🧠 Forma Orchestrator analyzing: \"%s\"\n\n", prompt)

		// Get absolute path to the executable to find internal scripts,
		// regardless of where the user is running the command from.
		exePath, err := os.Executable()
		if err != nil {
			return err
		}
		
		// The executable is either in /dist or /forma-cli, so we go up one directory
		baseDir := filepath.Dir(filepath.Dir(exePath))
		scriptPath := filepath.Join(baseDir, "src", "scripts", "orchestrator.py")
		
		if _, err := os.Stat(scriptPath); os.IsNotExist(err) {
			// Fallback if the user ran it directly from the repo root
			scriptPath = filepath.Join(filepath.Dir(exePath), "src", "scripts", "orchestrator.py")
		}

		out, err := exec.Command("python", scriptPath, prompt).CombinedOutput()
		if err != nil {
			// Fallback to python3
			out, err = exec.Command("python3", scriptPath, prompt).CombinedOutput()
		}
		
		if err != nil {
			return fmt.Errorf("engine error: %s\nPath used: %s", string(out), scriptPath)
		}

		fmt.Println(strings.TrimSpace(string(out)))
		fmt.Println("\n✅ Copy this mandate into your IDE or feed it to your LLM.")
		return nil
	},
}

func init() {
	rootCmd.AddCommand(orchestrateCmd)
}
