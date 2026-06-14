package exporter

import (
	"encoding/json"
	"fmt"
	"os"
	"strings"
)

func ExportSCSS(tokensPath string) error {
	data, err := os.ReadFile(tokensPath)
	if err != nil {
		return fmt.Errorf("MASTER.tokens.json not found — run a build first")
	}

	var tokens DesignSystem
	if err := json.Unmarshal(data, &tokens); err != nil {
		return err
	}

	var sb strings.Builder

	if len(tokens.Color) > 0 {
		for name, token := range tokens.Color {
			sb.WriteString(fmt.Sprintf("$color-%s: %s;\n", name, token.Value))
		}
	}

	if len(tokens.Typography) > 0 {
		for name, token := range tokens.Typography {
			sb.WriteString(fmt.Sprintf("$font-%s: %s, sans-serif;\n", name, token.Value))
		}
	}

	if len(tokens.Spacing) > 0 {
		for name, token := range tokens.Spacing {
			sb.WriteString(fmt.Sprintf("$spacing-%s: %s;\n", name, token.Value))
		}
	}

	return os.WriteFile("_tokens.scss", []byte(sb.String()), 0644)
}
