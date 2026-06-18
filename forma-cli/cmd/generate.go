package cmd

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"

	"github.com/spf13/cobra"
)

var generateCmd = &cobra.Command{
	Use:   "generate [project_name] [industry] [mood]",
	Short: "Generates the W3C Design System JSON tokens based on mathematical models",
	Long:  `Runs the Python Intelligence Engine to calculate OKLCH colors, fluid typography, and spacing scales. Saves output to design-system/MASTER.tokens.json`,
	Args:  cobra.ExactArgs(3),
	RunE: func(cmd *cobra.Command, args []string) error {
		projectName := args[0]
		industry := args[1]
		mood := args[2]

		fmt.Printf("🎨 Generating Advanced Design System for %s...\n", projectName)

		exePath, err := os.Executable()
		if err != nil {
			return err
		}

		baseDir := filepath.Dir(filepath.Dir(exePath))
		scriptPath := filepath.Join(baseDir, "src", "scripts", "design_system.py")

		if _, err := os.Stat(scriptPath); os.IsNotExist(err) {
			scriptPath = filepath.Join(filepath.Dir(exePath), "src", "scripts", "design_system.py")
		}

		out, err := exec.Command("python", scriptPath, projectName, industry, mood).CombinedOutput()
		if err != nil {
			out, err = exec.Command("python3", scriptPath, projectName, industry, mood).CombinedOutput()
		}

		if err != nil {
			return fmt.Errorf("engine error: %s\nPath used: %s", string(out), scriptPath)
		}

		// The python script handles its own output, we just echo it or confirm.
		fmt.Println("✅ Success! MASTER.tokens.json generated.")
		fmt.Println("👉 Next step: Run 'forma export' to compile these tokens into Tailwind configs.")
		return nil
	},
}

func init() {
	rootCmd.AddCommand(generateCmd)
}
