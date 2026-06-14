package cmd

import (
	"fmt"
	"os"

	"github.com/fzihak/forma/internal/healer"
	"github.com/spf13/cobra"
)

var healCmd = &cobra.Command{
	Use:   "heal [file]",
	Short: "AST-Driven Automated Healer for WCAG & Syntax",
	Long:  `Automatically scans and injects missing accessibility constraints (ARIA, Alts, SVGs) into frontend components in milliseconds without LLM cost.`,
	Args:  cobra.ExactArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		filePath := args[0]
		
		fmt.Printf("Analyzing component syntax: %s\n", filePath)

		result, err := healer.HealFile(filePath)
		if err != nil {
			fmt.Fprintf(os.Stderr, "Error: Failed to heal file - %v\n", err)
			os.Exit(1)
		}

		if result.WoundsHealed > 0 {
			fmt.Printf("✓ HEAL SUCCESS: Injected %d critical WCAG/Syntax constraints physically into the file.\n", result.WoundsHealed)
		} else {
			fmt.Printf("✓ COMPLIANT: Component passes strict heuristic checks. 0 wounds found.\n")
		}
	},
}

func init() {
	rootCmd.AddCommand(healCmd)
}
