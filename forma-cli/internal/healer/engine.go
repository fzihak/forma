package healer

import (
	"fmt"
	"os"
	"regexp"
	"strings"
)

type HealerResult struct {
	FilePath string
	WoundsHealed int
}

func HealFile(filePath string) (*HealerResult, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return nil, fmt.Errorf("could not read file: %v", err)
	}

	content := string(data)
	originalContent := content
	wounds := 0

	// Heuristic 1: Decorative SVGs need aria-hidden="true"
	// Match <svg ...> that don't already have aria-hidden
	svgRegex := regexp.MustCompile(`(<svg\b)([^>]*)(>)`)
	content = svgRegex.ReplaceAllStringFunc(content, func(match string) string {
		if !strings.Contains(match, "aria-hidden") && !strings.Contains(match, "role=\"img\"") {
			wounds++
			return strings.Replace(match, "<svg", "<svg aria-hidden=\"true\"", 1)
		}
		return match
	})

	// Heuristic 2: Images need alt attributes
	imgRegex := regexp.MustCompile(`(<img\b)([^>]*)(/?>)`)
	content = imgRegex.ReplaceAllStringFunc(content, func(match string) string {
		if !strings.Contains(match, "alt=") {
			wounds++
			return strings.Replace(match, "<img", "<img alt=\"Automated alt text\"", 1)
		}
		return match
	})

	// Heuristic 3: Buttons need aria-labels if they lack them
	buttonRegex := regexp.MustCompile(`(<button\b)([^>]*)(>)`)
	content = buttonRegex.ReplaceAllStringFunc(content, func(match string) string {
		if !strings.Contains(match, "aria-label") && !strings.Contains(match, "aria-labelledby") {
			wounds++
			return strings.Replace(match, "<button", "<button aria-label=\"Interactive Element\"", 1)
		}
		return match
	})

	if wounds > 0 && content != originalContent {
		err = os.WriteFile(filePath, []byte(content), 0644)
		if err != nil {
			return nil, fmt.Errorf("failed to write healed file: %v", err)
		}
	}

	return &HealerResult{
		FilePath:     filePath,
		WoundsHealed: wounds,
	}, nil
}
