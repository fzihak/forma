package healer

import (
	"fmt"
	"os"
	"strings"
)

type HealerResult struct {
	FilePath     string
	WoundsHealed int
}

// A simple JSX-aware lexer to inject attributes without breaking React syntax
func HealFile(filePath string) (*HealerResult, error) {
	data, err := os.ReadFile(filePath)
	if err != nil {
		return nil, fmt.Errorf("could not read file: %v", err)
	}

	content := string(data)
	originalContent := content
	wounds := 0

	// Targets for healing
	targets := map[string]struct {
		attr  string
		value string
		cond  func(tagContent string) bool
	}{
		"svg": {
			attr:  "aria-hidden",
			value: `"true"`,
			cond: func(s string) bool {
				return !strings.Contains(s, "aria-hidden") && !strings.Contains(s, "role=")
			},
		},
		"img": {
			attr:  "alt",
			value: `""`, // Decorative by default instead of meaningless text
			cond: func(s string) bool {
				return !strings.Contains(s, "alt=") && !strings.Contains(s, "alt={")
			},
		},
		"button": {
			attr:  "aria-label",
			value: `"button"`, // Empty strings are ignored by some SRs, use generic or nothing. Best is if we could derive it, but we fallback to a safe default.
			cond: func(s string) bool {
				return !strings.Contains(s, "aria-label") && !strings.Contains(s, "aria-labelledby")
			},
		},
	}

	var output strings.Builder
	output.Grow(len(content) + 500)

	i := 0
	for i < len(content) {
		if content[i] == '<' && i+1 < len(content) && isAlpha(content[i+1]) {
			// Start of a tag
			tagStart := i
			i++
			tagNameStart := i
			for i < len(content) && isAlphaNum(content[i]) {
				i++
			}
			tagName := strings.ToLower(content[tagNameStart:i])

			if target, exists := targets[tagName]; exists {
				// We found a target tag. Now find where the tag ends (handling strings and JSX {})
				inString := false
				var stringChar byte
				braceDepth := 0
				tagEnd := -1

				for j := i; j < len(content); j++ {
					c := content[j]
					if inString {
						if c == stringChar {
							inString = false
						}
					} else if braceDepth > 0 {
						if c == '{' {
							braceDepth++
						} else if c == '}' {
							braceDepth--
						}
					} else {
						if c == '"' || c == '\'' {
							inString = true
							stringChar = c
						} else if c == '{' {
							braceDepth++
						} else if c == '>' {
							tagEnd = j
							break
						} else if c == '/' && j+1 < len(content) && content[j+1] == '>' {
							tagEnd = j
							break
						}
					}
				}

				if tagEnd != -1 {
					tagContent := content[tagStart:tagEnd]
					if target.cond(tagContent) {
						// Inject attribute right after the tag name
						output.WriteString(content[tagStart:i])
						output.WriteString(" ")
						output.WriteString(target.attr)
						output.WriteString("=")
						output.WriteString(target.value)
						output.WriteString(content[i:tagEnd])
						i = tagEnd
						wounds++
					} else {
						output.WriteString(content[tagStart:i])
					}
				} else {
					output.WriteString(content[tagStart:i])
				}
			} else {
				output.WriteString(content[tagStart:i])
			}
		} else {
			output.WriteByte(content[i])
			i++
		}
	}

	finalContent := output.String()
	if wounds > 0 && finalContent != originalContent {
		err = os.WriteFile(filePath, []byte(finalContent), 0644)
		if err != nil {
			return nil, fmt.Errorf("failed to write healed file: %v", err)
		}
	}

	return &HealerResult{
		FilePath:     filePath,
		WoundsHealed: wounds,
	}, nil
}

func isAlpha(c byte) bool {
	return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')
}

func isAlphaNum(c byte) bool {
	return isAlpha(c) || (c >= '0' && c <= '9') || c == '-'
}
