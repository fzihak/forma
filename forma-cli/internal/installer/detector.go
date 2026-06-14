package installer

import "os"

func DetectPlatform() (string, error) {
    checks := []struct {
        path     string
        platform string
    }{
        {".claude", "claude"},
        {".cursor", "cursor"},
        {".windsurf", "windsurf"},
        {".github/copilot-instructions.md", "copilot"},
        {".continue", "continue"},
        {".kiro", "kiro"},
        {".roo", "roocode"},
    }

    for _, check := range checks {
        if _, err := os.Stat(check.path); err == nil {
            return check.platform, nil
        }
    }

    return "claude", nil
}
