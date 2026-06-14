package cmd

import (
    "fmt"
    "github.com/fzihak/forma/internal/exporter"
    "github.com/spf13/cobra"
)

var format string
var tokensPath string

var exportCmd = &cobra.Command{
    Use:   "export",
    Short: "Export Design Tokens to framework config",
    RunE: func(cmd *cobra.Command, args []string) error {
        if format == "tailwind" {
            err := exporter.ExportTailwind(tokensPath)
            if err == nil {
                fmt.Println("✓ Exported to tailwind.config.js")
            }
            return err
        } else if format == "css-vars" {
            err := exporter.ExportCSSVars(tokensPath)
            if err == nil {
                fmt.Println("✓ Exported to tokens.css")
            }
            return err
        } else if format == "scss" {
            err := exporter.ExportSCSS(tokensPath)
            if err == nil {
                fmt.Println("✓ Exported to _tokens.scss")
            }
            return err
        }
        return fmt.Errorf("unsupported format: %s", format)
    },
}

func init() {
    exportCmd.Flags().StringVar(&format, "format", "tailwind", "Export format (tailwind, css-vars, scss)")
    exportCmd.Flags().StringVar(&tokensPath, "path", "design-system/MASTER.tokens.json", "Path to MASTER.tokens.json")
    rootCmd.AddCommand(exportCmd)
}
