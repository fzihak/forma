package exporter

import (
    "encoding/json"
    "fmt"
    "os"
    "strings"
)

type DesignToken struct {
    Value string `json:"$value"`
    Type  string `json:"$type"`
}

// Support unmarshalling the nested advanced structure from Phase 3
type DesignSystem struct {
    Color      map[string]DesignToken `json:"color"`
    Typography map[string]DesignToken `json:"typography"`
    Spacing    map[string]DesignToken `json:"spacing"`
}

func ExportTailwind(tokensPath string) error {
    data, err := os.ReadFile(tokensPath)
    if err != nil {
        return fmt.Errorf("MASTER.tokens.json not found — run a build first")
    }

    var tokens DesignSystem
    if err := json.Unmarshal(data, &tokens); err != nil {
        return err
    }

    var sb strings.Builder
    sb.WriteString("/** @type {import('tailwindcss').Config} */\n")
    sb.WriteString("module.exports = {\n  theme: {\n    extend: {\n")

    if len(tokens.Color) > 0 {
        sb.WriteString("      colors: {\n")
        for name, token := range tokens.Color {
            sb.WriteString(fmt.Sprintf("        '%s': '%s',\n", name, token.Value))
        }
        sb.WriteString("      },\n")
    }

    if len(tokens.Typography) > 0 {
        sb.WriteString("      fontFamily: {\n")
        for name, token := range tokens.Typography {
            sb.WriteString(fmt.Sprintf("        '%s': ['%s', 'sans-serif'],\n", name, token.Value))
        }
        sb.WriteString("      },\n")
    }

    if len(tokens.Spacing) > 0 {
        sb.WriteString("      spacing: {\n")
        for name, token := range tokens.Spacing {
            sb.WriteString(fmt.Sprintf("        '%s': '%s',\n", name, token.Value))
        }
        sb.WriteString("      },\n")
    }

    sb.WriteString("    },\n  },\n}\n")

    return os.WriteFile("tailwind.config.js", []byte(sb.String()), 0644)
}
