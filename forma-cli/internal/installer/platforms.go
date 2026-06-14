package installer

type Platform struct {
    Name        string
    SkillDir    string
    GlobalDir   string
    Mode        string
    ConfigFile  string
}

var Platforms = map[string]Platform{
    "claude": {
        Name:      "Claude Code",
        SkillDir:  ".claude/skills/forma",
        GlobalDir: "~/.claude/skills/forma",
        Mode:      "auto",
    },
    "cursor": {
        Name:      "Cursor",
        SkillDir:  ".cursor/rules/forma",
        GlobalDir: "~/.cursor/rules/forma",
        Mode:      "auto",
    },
    "windsurf": {
        Name:      "Windsurf",
        SkillDir:  ".windsurf/rules/forma",
        GlobalDir: "~/.windsurf/rules/forma",
        Mode:      "auto",
    },
    "copilot": {
        Name:       "GitHub Copilot",
        SkillDir:   ".github",
        ConfigFile: ".github/copilot-instructions.md",
        Mode:       "auto",
    },
    "continue": {
        Name:      "Continue",
        SkillDir:  ".continue/skills/forma",
        GlobalDir: "~/.continue/skills/forma",
        Mode:      "auto",
    },
    "kiro": {
        Name:     "Kiro",
        SkillDir: ".kiro/workflows",
        Mode:     "slash-command",
    },
    "roocode": {
        Name:     "Roo Code",
        SkillDir: ".roo/workflows",
        Mode:     "slash-command",
    },
}
