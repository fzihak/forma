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

## 📑 Table of Contents
- [The Vision](#-the-vision)
- [Core Features](#-core-features)
- [System Architecture](#️-system-architecture)
- [Quick Start](#-quick-start)
- [Usage Examples](#-usage-examples)
- [CLI Reference](#️-cli-reference)
- [Compatibility](#️-compatibility)
- [Security & Privacy](#-security--privacy)
- [Contributing](#-contributing)

---

## ⚡ The Vision

Every AI coding assistant today answers the same question: > *"How should this look?"*

Color palettes. Font pairings. Useful—but fundamentally shallow. Real, industry-grade design requires asking harder questions before a single line of code is written:

- *Who is this for, and what do they actually need?*
- *What does this specific industry strictly forbid?*
- *What cognitive psychology drives this user's decisions?*
- *Will this actually convert?*

**Forma** is built to answer all of them. Automatically. In sequence.

<br/>

## 💎 Core Features

Forma operates at the absolute pinnacle of AI software engineering. It is not just a prompt file—it is a secure, multi-language execution environment powered by Python and Go.

### 🧠 12-Layer Reasoning System
Before any UI is generated, Forma forces your AI through a sequential gauntlet. It analyzes the UX Pre-Flight, queries Industry Intelligence, cross-references Cognitive Psychology, applies Component Best Practices, and performs an Accessibility Audit. Only then does it write code.

### 🩺 AST-Driven Auto-Healer (Zero-Token Healing)
Instead of forcing the AI to waste thousands of tokens rewriting an entire React component just to fix a missing `aria-label`, the Forma Critic agent triggers the Go-based Auto-Healer (`forma heal <file>`). The CLI physically parses your frontend AST and surgically injects missing ARIA labels, alt texts, and SVG properties in **milliseconds**.

### 📐 Mathematical W3C Tokens
Every generated design system is backed by advanced mathematics (OKLCH Color Spaces, Fluid `clamp()` Typography, and Spring Physics) and exported directly into the global W3C Design Token format.

### 🛡️ Graceful Halting
Forma will never catastrophically crash on a developer's machine. The `forma doctor` command instantly diagnoses your environment. If it detects a system failure, it triggers a **Graceful Halt** rather than hallucinating bad code.

<br/>

## 🏗️ System Architecture

Forma is powered by a dual-engine architecture: a high-speed Go CLI that manages system states, and a Python Intelligence Engine that processes complex reasoning matrices.

```mermaid
graph TD
    A[User Prompt in IDE] --> B{Forma Agent}
    B -->|Calls| C[Python Intelligence Engine]
    C --> D[12-Layer Reasoning Matrix]
    D --> E[Industry Rulesets]
    D --> F[Psychology Triggers]
    D --> G[Accessibility Audit]
    G --> B
    B -->|Generates| H[Frontend Code]
    H --> I[Forma Critic]
    I -->|Detects WCAG issues| J[Go CLI: forma heal]
    J -->|AST Injection| H
    classDef primary fill:#6366F1,stroke:#fff,stroke-width:2px,color:#fff;
    classDef secondary fill:#8B5CF6,stroke:#fff,stroke-width:2px,color:#fff;
    classDef engine fill:#10B981,stroke:#fff,stroke-width:2px,color:#fff;
    class B primary;
    class C engine;
    class D,E,F,G secondary;
```

<br/>

## 🔬 Research & Data Methodology

Forma is built on a foundation of peer-reviewed UX research, mathematical color spaces, and cognitive psychology. It is not an LLM hallucinating designs; it is an LLM querying a strict, deterministic database.

### The Automated Reasoning Sequence
When you prompt your IDE, Forma executes a massive background sequence before writing any code:

```mermaid
sequenceDiagram
    participant Dev as IDE Developer
    participant Forma as Forma Engine
    participant DB as Knowledge Matrix
    participant Output as Generated UI

    Dev->>Forma: "Build a high-converting pricing table"
    activate Forma
    Forma->>DB: Query Psychology Triggers (SaaS)
    DB-->>Forma: Inject: [Decoy Effect, Anchoring]
    Forma->>DB: Query Accessibility (WCAG 2.2 AAA)
    DB-->>Forma: Enforce: [Contrast > 7:1, aria-labelledby]
    Forma->>DB: Map Mathematical Tokens
    DB-->>Forma: Export: [OKLCH Fluid Space]
    Forma-->>Output: Compile Validated UI Component
    deactivate Forma
    Output-->>Dev: Production-Ready Code
```

### Applied Cognitive Psychology
Forma maps UI component generation directly to established psychological triggers to maximize user retention, trust, and conversion rates.

| Cognitive Trigger | UI Execution Strategy | Primary Industry |
| :--- | :--- | :--- |
| **Hick's Law** | Progressive disclosure & automated layout reduction | SaaS, E-Commerce |
| **Zeigarnik Effect** | Step-based visual progress rings & incomplete states | EdTech, Gamification |
| **Von Restorff Effect** | OKLCH chroma-isolation for primary Call-to-Actions | Fintech, Marketing |
| **Cognitive Load Theory** | Fluid whitespace scaling via Golden Ratio algorithms | Healthcare, Dashboards |

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

<br/>

## 💡 Usage Examples

Once installed, Forma operates silently in the background. Just talk to your AI naturally. Forma intercepts the visual requests and applies its reasoning layers.

**Example 1: High-Converting SaaS**
> *"Build a pricing page for our B2B SaaS. Ensure it uses the 'Scarcity' psychology trigger and passes WCAG AAA contrast."*

**Example 2: Industry-Specific Design**
> *"Create a checkout flow for a Fintech app. Forma, check your industry rules for traditional banking before generating."*

**Example 3: Mathematical Redesign**
> *"Refactor this dashboard. Generate a fluid typography scale using `clamp()` and an OKLCH color system."*

<br/>

## 🛠️ CLI Reference

The `forma-cli` binary is lightning fast and handles all environment integrations.

| Command | Description |
| :--- | :--- |
| `forma init` | Interactively configures AI agents and installs Python dependencies (beautifulsoup4, lxml). |
| `forma orchestrate "<prompt>"` | Compiles UX psychology rules and W3C constraints based on user prompt. |
| `forma generate <project> <industry> <mood>` | Runs the Mathematical Engine to generate fluid OKLCH Design Tokens. |
| `forma export --format tailwind` | Compiles the generated W3C tokens into your frontend's `tailwind.config.js`. |
| `forma audit <path>` | Scans UI files using the Critic Engine to grade WCAG, UX, and Visual Hierarchy. |
| `forma heal <file>` | Triggers the AST Auto-Healer to physically inject missing WCAG code. |
| `forma doctor` | Runs a system diagnostic on your Python and Go environments. |
| `forma update` | Instantly upgrades the CLI to the latest Vanguard release from GitHub. |
| `forma remove` | Safely purges Forma agents from your codebase. |

<br/>

## ⚙️ Compatibility

### Supported IDEs / Agents

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

<br/>

## 🔒 Security & Privacy

Forma is built for Enterprise, which means privacy is non-negotiable.

- **Zero Telemetry**: Forma does not track your usage, collect your prompts, or phone home.
- **Local Execution**: The Go CLI and Python Engine run entirely on your local machine.
- **Sandboxed Agent Logic**: All AI requests are handled exclusively by your IDE's existing LLM connections. Forma acts merely as local context and tooling.

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
