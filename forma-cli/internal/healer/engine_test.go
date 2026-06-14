package healer

import (
	"os"
	"path/filepath"
	"strings"
	"testing"
)

func TestHealFile(t *testing.T) {
	// Create a temporary file to simulate a broken React component
	tempDir := t.TempDir()
	filePath := filepath.Join(tempDir, "BrokenComponent.jsx")
	
	brokenContent := `
export default function Test() {
	return (
		<div>
			<img src="/logo.png" />
			<button className="btn">
				<svg viewBox="0 0 24 24"><path d="M5 12h14" /></svg>
			</button>
		</div>
	)
}
`
	err := os.WriteFile(filePath, []byte(brokenContent), 0644)
	if err != nil {
		t.Fatalf("Failed to create temp file: %v", err)
	}

	result, err := HealFile(filePath)
	if err != nil {
		t.Fatalf("HealFile failed: %v", err)
	}

	if result.WoundsHealed != 3 {
		t.Errorf("Expected 3 wounds healed, got %d", result.WoundsHealed)
	}

	// Verify the healed content
	healedContent, err := os.ReadFile(filePath)
	if err != nil {
		t.Fatalf("Failed to read healed file: %v", err)
	}
	contentStr := string(healedContent)

	if !strings.Contains(contentStr, `img alt="Automated alt text"`) {
		t.Errorf("IMG tag was not healed correctly.")
	}
	if !strings.Contains(contentStr, `button aria-label="Interactive Element"`) {
		t.Errorf("BUTTON tag was not healed correctly.")
	}
	if !strings.Contains(contentStr, `svg aria-hidden="true"`) {
		t.Errorf("SVG tag was not healed correctly.")
	}
}
