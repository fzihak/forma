package cmd

import (
    "os"
    "github.com/spf13/cobra"
)

var rootCmd = &cobra.Command{
    Use:   "forma",
    Short: "Forma — The AI skill that reasons before it designs",
    Long:  `Forma is a Design Intelligence Framework that installs deep design reasoning into AI coding assistants.`,
}

func Execute() {
    err := rootCmd.Execute()
    if err != nil {
        os.Exit(1)
    }
}
