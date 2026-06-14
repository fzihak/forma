<div align="center">

<img src="https://raw.githubusercontent.com/fzihak/forma/main/.github/assets/banner.png" alt="Forma Vanguard Framework" width="100%" />

# 📐 FORMA
**The AI skill that reasons before it designs.**

[![Build Status](https://img.shields.io/github/actions/workflow/status/fzihak/forma/release.yml?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/fzihak/forma/actions/workflows/release.yml)
[![NPM version](https://img.shields.io/npm/v/@foysalzihak/forma-cli?style=for-the-badge&color=CB3837&logo=npm)](https://www.npmjs.com/package/@foysalzihak/forma-cli)
[![Architecture](https://img.shields.io/badge/Architecture-Vanguard_V3-6366F1?style=for-the-badge&logo=polkadot)](https://github.com/fzihak/forma)
[![Reasoning Layers](https://img.shields.io/badge/Layers-12-8B5CF6?style=for-the-badge)]()
[![Industries](https://img.shields.io/badge/Industries-16-10B981?style=for-the-badge)]()
[![License](https://img.shields.io/github/license/fzihak/forma?style=for-the-badge&color=3B82F6)](LICENSE)

<br/>

*Forma is an open-source Design Intelligence Framework for AI coding assistants. It replaces basic "generate UI" prompts with an enterprise-grade, multi-agent reasoning architecture.*

</div>

---

## ⚡ The Problem

Every AI coding assistant today answers the same question: > *"How should this look?"*

Color palettes. Font pairings. Useful—but fundamentally shallow. Real, industry-grade design requires asking harder questions before a single line of code is written:

- *Who is this for, and what do they actually need?*
- *What does this specific industry strictly forbid?*
- *What cognitive psychology drives this user's decisions?*
- *Will this actually convert?*

**Forma** is built to answer all of them. Automatically. In sequence.

<br/>

## 🧠 The Vanguard Architecture (V3)

Forma operates at the absolute pinnacle of AI software engineering. It is not just a prompt file—it is a secure, multi-language execution environment powered by Python and Go.

<details>
<summary><b>1️⃣ 12-Layer Reasoning System</b></summary>
<br>
Before any UI is generated, Forma forces your AI through a sequential gauntlet:
UX Pre-Flight → Industry Intelligence → Psychology Analysis → Component Best Practices → Accessibility Audit → Output.
</details>

<details>
<summary><b>2️⃣ AST-Driven Auto-Healer (Zero-Token Healing)</b></summary>
<br>
Instead of forcing the AI to waste thousands of tokens rewriting an entire React component just to fix a missing `aria-label`, the Forma Critic agent triggers the Go-based Auto-Healer (`forma heal <file>`). The CLI physically reads your frontend code and surgically injects missing ARIA labels, alt texts, and SVG properties in <b>milliseconds</b>.
</details>

<details>
<summary><b>3️⃣ W3C Design Token Engine</b></summary>
<br>
Every generated design system is backed by advanced mathematics (OKLCH Color Spaces, Fluid `clamp()` Typography, and Spring Physics) and exported directly into the global W3C Design Token format.
</details>

<details>
<summary><b>4️⃣ Diagnostic Resilience & Graceful Halts</b></summary>
<br>
Forma will never catastrophically crash on a developer's machine. The `forma doctor` command instantly diagnoses your environment. If it detects a system failure, it triggers a <b>Graceful Halt</b> rather than hallucinating bad code.
</details>

<br/>

## 🚀 Quick Start

**Requirements:** Node.js 18+ · Python 3.9+ · A supported AI assistant

#### 1. Install Globally (NPM)
```bash
npm install -g @foysalzihak/forma-cli
```

#### 2. Inject into your IDE
```bash
forma init --ai claude       # Claude Code
forma init --ai cursor       # Cursor
forma init --ai windsurf     # Windsurf
forma init --ai all          # Install everywhere
```

#### 3. Talk to your AI normally
Install it once, then just talk to your IDE like you always have.
> *"Build a fintech SaaS dashboard with a dark theme."*
> *"Review this checkout UI for conversion and accessibility issues."*

<br/>

## 🛠️ CLI Toolkit

The `forma-cli` binary is lightning fast and handles all environment integrations.

| Command | Description |
| :--- | :--- |
| `forma doctor` | Runs a system diagnostic on your Python and Go environments. |
| `forma heal <file>` | Triggers the AST Auto-Healer to physically inject missing WCAG code. |
| `forma export --format tailwind` | Exports the W3C tokens into your Tailwind configuration. |
| `forma update` | Instantly upgrades the CLI to the latest Vanguard release. |
| `forma remove` | Safely purges Forma agents from your codebase. |

<br/>

## 🛡️ Compatibility

### Supported IDEs

| Agent Platform | Support | Installation Command |
| :--- | :---: | :--- |
| ![Agent](https://img.shields.io/badge/Agent-0A0A0A?style=for-the-badge) | ✅ | `forma init --ai agent` |
| ![Augment](https://img.shields.io/badge/Augment-FF4500?style=for-the-badge) | ✅ | `forma init --ai augment` |
| ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=for-the-badge&logo=anthropic&logoColor=white) | ✅ | `forma init --ai claude` |
| ![Codebuddy](https://img.shields.io/badge/Codebuddy-10B981?style=for-the-badge) | ✅ | `forma init --ai codebuddy` |
| ![Codex](https://img.shields.io/badge/Codex-000000?style=for-the-badge) | ✅ | `forma init --ai codex` |
| ![Continue](https://img.shields.io/badge/Continue.dev-2088FF?style=for-the-badge) | ✅ | `forma init --ai continue` |
| ![GitHub Copilot](https://img.shields.io/badge/GitHub_Copilot-181717?style=for-the-badge&logo=github&logoColor=white) | ✅ | `forma init --ai copilot` |
| ![Cursor](https://img.shields.io/badge/Cursor-000000?style=for-the-badge&logo=openai&logoColor=white) | ✅ | `forma init --ai cursor` |
| ![Droid](https://img.shields.io/badge/Droid-3DDC84?style=for-the-badge&logo=android&logoColor=white) | ✅ | `forma init --ai droid` |
| ![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white) | ✅ | `forma init --ai gemini` |
| ![Kilocode](https://img.shields.io/badge/Kilocode-6366F1?style=for-the-badge) | ✅ | `forma init --ai kilocode` |
| ![Kiro](https://img.shields.io/badge/Kiro-FF3366?style=for-the-badge) | ✅ | `forma init --ai kiro` |
| ![OpenCode](https://img.shields.io/badge/OpenCode-0A0A0A?style=for-the-badge) | ✅ | `forma init --ai opencode` |
| ![Qoder](https://img.shields.io/badge/Qoder-F59E0B?style=for-the-badge) | ✅ | `forma init --ai qoder` |
| ![Roo Code](https://img.shields.io/badge/Roo_Code-6B21A8?style=for-the-badge) | ✅ | `forma init --ai roocode` |
| ![Trae](https://img.shields.io/badge/Trae-3B82F6?style=for-the-badge) | ✅ | `forma init --ai trae` |
| ![Warp](https://img.shields.io/badge/Warp-01A4FF?style=for-the-badge) | ✅ | `forma init --ai warp` |
| ![Windsurf](https://img.shields.io/badge/Windsurf-0EA5E9?style=for-the-badge) | ✅ | `forma init --ai windsurf` |

<br/>

### Supported Frameworks

Forma is universally adaptable. Just mention your stack in the prompt, or let it intelligently default to HTML + Tailwind CSS.

| Icon | Framework | Domain |
| :---: | :--- | :--- |
| <img src="https://skillicons.dev/icons?i=react" width="28"/> | **React** | Web UI Library |
| <img src="https://skillicons.dev/icons?i=nextjs" width="28"/> | **Next.js** | Web Fullstack Framework |
| <img src="https://skillicons.dev/icons?i=vue" width="28"/> | **Vue.js** | Web UI Library |
| <img src="https://skillicons.dev/icons?i=nuxtjs" width="28"/> | **Nuxt.js** | Web Fullstack Framework |
| <img src="https://skillicons.dev/icons?i=svelte" width="28"/> | **Svelte** | Web Compiler |
| <img src="https://skillicons.dev/icons?i=astro" width="28"/> | **Astro** | Static Site Generator |
| <img src="https://skillicons.dev/icons?i=angular" width="28"/> | **Angular** | Web Framework |
| <img src="https://skillicons.dev/icons?i=solidjs" width="28"/> | **SolidJS** | Web UI Library |
| <img src="https://skillicons.dev/icons?i=remix" width="28"/> | **Remix** | Web Fullstack Framework |
| <img src="https://skillicons.dev/icons?i=tailwind" width="28"/> | **Tailwind CSS** | Global Styling System |
| <img src="https://skillicons.dev/icons?i=bootstrap" width="28"/> | **Bootstrap** | CSS Framework |
| <img src="https://skillicons.dev/icons?i=materialui" width="28"/> | **Material UI** | Component Library |
| <img src="https://skillicons.dev/icons?i=flutter" width="28"/> | **Flutter** | Cross-Platform Mobile |
| <img src="https://skillicons.dev/icons?i=react" width="28"/> | **React Native** | Cross-Platform Mobile |
| <img src="https://skillicons.dev/icons?i=swift" width="28"/> | **SwiftUI** | iOS Native |
| <img src="https://skillicons.dev/icons?i=kotlin" width="28"/> | **Jetpack Compose** | Android Native |
| <img src="https://skillicons.dev/icons?i=laravel" width="28"/> | **Laravel** | PHP Fullstack Framework |
| <img src="https://skillicons.dev/icons?i=django" width="28"/> | **Django** | Python Fullstack Framework |
| <img src="https://skillicons.dev/icons?i=ruby" width="28"/> | **Ruby on Rails** | Ruby Fullstack Framework |
| <img src="https://skillicons.dev/icons?i=express" width="28"/> | **Express.js** | Node.js Backend Framework |
| <img src="https://skillicons.dev/icons?i=spring" width="28"/> | **Spring Boot** | Java Backend Framework |

<br/>

## 🧼 Uninstallation

Forma deeply respects your codebase. If you want to remove the AI logic from your project, you don't have to hunt down hidden files.

```bash
# 1. Safely purge all Forma agents from your repository
forma remove

# 2. Uninstall the global binary
npm uninstall -g @foysalzihak/forma-cli
```

<br/>

## 🤝 Contributing

We welcome contributions from the community! Forma is a dual-engine framework built with **Go** (CLI) and **Python** (Intelligence).

```bash
# Clone the repository
git clone https://github.com/fzihak/forma.git
cd forma

# Run the Automated Test Suite
cd forma-cli
go test ./internal/healer/...
python -m unittest ../src/tests/test_engine.py
```

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for full architectural guidelines.

---
<div align="center">
  <p>Built with <b>Go</b>, <b>Python</b>, and <b>Mathematical Neuro-Design</b>.</p>
  <p>MIT License © Foysal Zihak</p>
</div>
