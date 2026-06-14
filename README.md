<div align="center">

# Forma

### The AI skill that reasons before it designs.

[![License](https://img.shields.io/github/license/fzihak/forma?style=flat-square&color=0A0A0A)](LICENSE)
[![Architecture](https://img.shields.io/badge/architecture-Vanguard_V3-0A0A0A?style=flat-square)]()
[![Reasoning Layers](https://img.shields.io/badge/reasoning%20layers-12-0A0A0A?style=flat-square)]()
[![Industries](https://img.shields.io/badge/industries-16-0A0A0A?style=flat-square)]()
[![Platforms](https://img.shields.io/badge/platforms-7-0A0A0A?style=flat-square)]()
[![NPM version](https://img.shields.io/npm/v/forma-cli?style=flat-square&color=0A0A0A)](https://www.npmjs.com/package/forma-cli)

</div>

---

## The gap no one is talking about

Every AI design skill today answers the same question:

> *"How should this look?"*

Color palettes. Font pairings. Style recommendations. Useful — but shallow.

Real design requires asking harder questions before a single line of code is written:

- *Who is this for, and what do they actually need?*
- *What does this industry require — and strictly forbid?*
- *What psychology drives this user's decisions?*
- *Will this be consistent with what we built last month?*
- *Does this hold up for someone on a screen reader?*
- *Will this actually convert?*

**Forma** is built to answer all of them — automatically, in sequence, before generating any UI.

---

## What Forma is

Forma is an open-source **Design Intelligence Framework** for AI coding assistants.

It installs as a skill into Claude Code, Cursor, Windsurf, and others. Once installed, it replaces the one-step "generate UI" pattern with a structured, multi-layer reasoning system that plans, researches, builds, audits, and physically heals its own code.

**Without Forma**

```
Your prompt  →  AI generates UI
```

**With Forma**

```
Your prompt
      │
      ▼
Trigger detection — only the relevant layers activate
      │
      ▼
UX Pre-Flight — audience, goals, risks, information architecture
      │
      ▼
Industry Intelligence — what this domain requires and forbids
      │
      ▼
Psychology Analysis — trust signals, conversion, cognitive load
      │
      ▼
Design System Generation — typography, color, spacing, W3C tokens
      │
      ▼
Component Selection — best practices, anti-patterns, industry variants
      │
      ▼
UI Generation — framework-aware, token-driven
      │
      ▼
Accessibility Audit — WCAG AA automated checks
      │
      ▼
AST Auto-Healing — Go CLI physically injects missing syntax in 10ms
      │
      ▼
Output
```

---

## Vanguard Architecture (V3)

Forma operates at the absolute pinnacle of AI software engineering. It is not just a prompt file—it is a secure, multi-language execution environment.

### 1. AST-Driven Auto-Healer
Instead of forcing the AI to waste thousands of tokens rewriting an entire React/Vue component just to fix a missing `aria-label`, the Forma Critic agent triggers the Go-based Auto-Healer (`forma heal <file>`). The CLI physically reads your frontend code and surgically injects missing ARIA labels, alt texts, and SVG properties in **milliseconds** without using a single API token.

### 2. Diagnostic Resilience
Forma will never catastrophically crash on a developer's machine. The `forma doctor` command instantly diagnoses your Python environment and directory permissions. If the AI detects a system failure, it triggers a **Graceful Halt** rather than hallucinating bad code.

### 3. W3C Design Token Engine
Every generated design system is backed by advanced mathematics (OKLCH Color Spaces, Fluid `clamp()` Typography, and Spring Physics) and exported directly into the [W3C Design Token](https://design-tokens.github.io/community-group/format/) format. 

```json
{
  "$schema": "https://design-tokens.org/schema.json",
  "color": {
    "primary":    { "$value": "oklch(0.6 0.15 250)", "$type": "color" }
  },
  "physics": {
    "snappy": { "stiffness": 400, "damping": 30, "$type": "spring" }
  }
}
```

---

## Installation

**Requirements:** Node.js 18+ · Python 3.9+ · A supported AI assistant

Forma is distributed globally via NPM and GitHub Actions.

```bash
# 1. Install the CLI wrapper globally
npm install -g forma-cli

# 2. Install the agents into your IDE
forma init --ai claude       # Claude Code
forma init --ai cursor       # Cursor
forma init --ai windsurf     # Windsurf
forma init --ai copilot      # GitHub Copilot
forma init --ai continue     # Continue
forma init --ai all          # Install to all supported IDEs

# (Optional) Install globally for all future projects
forma init --ai cursor --global
```

### CLI Commands

```bash
forma doctor                       # Run system diagnostics
forma update                       # Upgrade to the latest Forma release
forma export --format tailwind     # Export W3C tokens to Tailwind config
forma export --format css-vars     # Export W3C tokens to CSS variables
forma heal <file>                  # Trigger the AST Auto-Healer on a file
forma remove                       # Safely purge Forma from the repository
```

---

## Usage

Install once. Then just talk to your AI assistant the way you always have.

```
Build a fintech SaaS dashboard with dark theme
```

```
Design a landing page for a healthcare appointment platform
```

```
Review this checkout UI for conversion and accessibility issues
```

The right layers activate automatically based on what you asked. You get enterprise-grade output without changing how you work.

---

## Supported platforms

| Platform | Activation | Path |
|---|---|---|
| Claude Code | Automatic | `.claude/skills/` |
| Cursor | Automatic | `.cursor/rules/` |
| Windsurf | Automatic | `.windsurf/rules/` |
| GitHub Copilot | Automatic | `.github/copilot-instructions.md` |
| Continue | Automatic | `.continue/skills/` |
| Kiro | `/forma` command | workflow file |
| Roo Code | `/forma` command | workflow file |

---

## Supported frameworks

React · Next.js · Vue · Nuxt.js · Svelte · Astro · HTML + Tailwind · shadcn/ui · SwiftUI · Jetpack Compose · React Native · Flutter · Laravel

Mention your stack in the prompt or let Forma default to HTML + Tailwind.

---

## Uninstallation

Forma respects your codebase. If you want to remove the AI logic from your project, you don't have to hunt down hidden files.

```bash
# 1. Safely purge all Forma agents from your repository
forma remove

# 2. Uninstall the global binary
npm uninstall -g forma-cli
```

---

## Contributing

We welcome contributions from the community! Forma is built with Go (CLI) and Python (Intelligence Engine).

```bash
git clone https://github.com/fzihak/forma.git
cd forma

# Test locally without downloading binaries
cd forma-cli
go run main.go init --ai claude --offline

# Run Automated Test Suite
go test ./internal/healer/...
python -m unittest src/tests/test_engine.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

<div align="center">

Built with **Go**, **Python**, and **Mathematical Neuro-Design**.

</div>
