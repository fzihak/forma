# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Forma is a Design Intelligence Framework for AI coding assistants. Instead of jumping straight to UI, it makes your AI assistant think like a design team — researching the audience, applying industry constraints, generating a design system, building the interface, then auditing and critiquing its own work.

## Architecture

```
src/
├── knowledge/          # Core design intelligence data (JSON)
│   ├── ui_styles.json, color_systems.json, typography.json
│   ├── reasoning_rules.json, design_patterns.json, ux_guidelines.json
├── industries/         # 163 industry-specific constraint files
├── psychology/         # Conversion psychology triggers
├── components/         # Component intelligence library
├── scripts/            # Python tooling
│   ├── search.py       # BM25 search engine
│   ├── design_system.py # Design system generator (W3C tokens)
│   ├── trigger.py      # Multi-agent trigger logic
│   ├── token_bridge.py # Token → Tailwind/CSS/SCSS export
│   └── test_suite.py
└── tokens/output/

agents/                 # Multi-agent instruction files
├── architect.md, researcher.md, psychologist.md
├── component.md, accessibility.md, critic.md, frontend.md

design-system/          # Generated output (project-owned)
├── MASTER.md           # Human-readable design system
├── MASTER.tokens.json  # W3C Design Token format
└── pages/

forma-cli/              # Go CLI binary (forma)
├── cmd/                # Cobra commands (init, export, heal, doctor, remove)
├── internal/
│   ├── assets/files/   # Embedded skill files (go:embed)
│   ├── installer/      # Platform detection + file installation/removal
│   ├── healer/         # AST-Driven Auto-Healer engine
│   ├── diagnostic/     # System environment diagnostics
│   ├── updater/        # GitHub async auto-updater
│   └── exporter/       # Token → framework config export

bin/                    # NPM wrapper scripts (forma.js, install.js)
package.json            # NPM registry package configuration

templates/
├── base/               # SKILL.md template
└── platforms/           # Platform-specific config JSONs
```

## Key Commands

**Search:**
```bash
python src/scripts/search.py "<query>"
```

**Generate design system:**
```bash
python src/scripts/design_system.py "<project_name>" "<industry>" "<mood>"
```

**Trigger agents:**
```bash
python src/scripts/trigger.py "<user_prompt>"
```

**Token export:**
```bash
python src/scripts/token_bridge.py tailwind design-system/MASTER.tokens.json
python src/scripts/token_bridge.py css-vars design-system/MASTER.tokens.json
python src/scripts/token_bridge.py scss design-system/MASTER.tokens.json
```

**CLI (Go/NPM):**
```bash
npm install -g forma-cli           # Install globally via NPM wrapper
forma init --ai claude             # Install agents
forma doctor                       # Run system diagnostics
forma heal src/app/page.tsx        # Trigger the AST auto-healer
forma export --format tailwind     # Export design tokens
forma remove                       # Safely purge Forma from the project
```

## Prerequisites

- Python 3.x (no external dependencies)
- Go 1.22+ (for CLI development)

## Git Workflow

Never push directly to `main`. Always:

1. Create a new branch: `git checkout -b feat/...` or `fix/...`
2. Commit changes
3. Push branch: `git push -u origin <branch>`
4. Create PR: `gh pr create`
