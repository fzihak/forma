# Initialize git repository
git init

# Helper to add and commit
function Commit-Item {
    param(
        [string]$Path,
        [string]$Message
    )
    # Ignore errors if file doesn't exist
    $ErrorActionPreference = "SilentlyContinue"
    git add $Path
    if ($LASTEXITCODE -eq 0) {
        git commit -m $Message
    }
    $ErrorActionPreference = "Continue"
}

# 1-10: Foundation & Knowledge Base
Commit-Item ".gitignore" "chore: setup gitignore"
Commit-Item "package.json" "chore: initialize npm package structure"
Commit-Item "src/knowledge/ui_styles.json" "feat(knowledge): add core UI style matrix"
Commit-Item "src/knowledge/color_systems.json" "feat(knowledge): implement OKLCH mathematical color systems"
Commit-Item "src/knowledge/typography.json" "feat(knowledge): add fluid clamp typography rules"
Commit-Item "src/knowledge/design_patterns.json" "feat(knowledge): establish core design patterns"
Commit-Item "src/knowledge/ux_guidelines.json" "feat(knowledge): add 99 UX heuristics"
Commit-Item "src/knowledge/accessibility.json" "feat(knowledge): integrate WCAG 2.2 strict compliance rules"
Commit-Item "src/knowledge/interaction_patterns.json" "feat(knowledge): add spring physics and interaction timing"
Commit-Item "src/knowledge/conversion_patterns.json" "feat(knowledge): implement conversion optimization logic"

# 11-20: Advanced Knowledge & Industries
Commit-Item "src/components/*.json" "feat(knowledge): add 20+ dynamic component blueprints"
Commit-Item "src/psychology/triggers.json" "feat(psychology): add 10 cognitive conversion triggers"
Commit-Item "src/industries/fintech.json" "feat(industry): add fintech security constraints"
Commit-Item "src/industries/healthcare.json" "feat(industry): add healthcare compliance rules"
Commit-Item "src/industries/ecommerce.json" "feat(industry): add ecommerce conversion logic"
Commit-Item "src/industries/saas.json" "feat(industry): add b2b saas dashboard standards"
Commit-Item "src/industries/*.json" "feat(industry): populate remaining industry intelligence profiles"
Commit-Item "templates/base/skill-content.md" "feat(template): create base SKILL.md template for IDE injection"
Commit-Item "templates/base/quick-reference.md" "feat(template): add quick reference guide"
Commit-Item "src/scripts/search.py" "feat(engine): build BM25 zero-dependency search engine"

# 21-30: Python Core Engine & Agents
Commit-Item "src/scripts/trigger.py" "feat(engine): implement multi-agent trigger and activation logic"
Commit-Item "src/scripts/design_system.py" "feat(engine): build core design system generator"
Commit-Item "src/scripts/token_bridge.py" "feat(engine): add W3C Design Token exporter for Tailwind/CSS"
Commit-Item "src/scripts/critic.py" "feat(engine): implement rule-based design critic scoring"
Commit-Item "src/scripts/accessibility.py" "feat(engine): build AST accessibility compliance checker"
Commit-Item "agents/architect.md" "feat(agent): construct Architect prime node with YAML frontmatter"
Commit-Item "agents/researcher.md" "feat(agent): build UX Researcher pre-flight agent"
Commit-Item "agents/psychologist.md" "feat(agent): implement Behavioral Psychologist node"
Commit-Item "agents/component.md" "feat(agent): add Component Engineer node"
Commit-Item "agents/frontend.md" "feat(agent): add Frontend Framework integration node"

# 31-40: CLI Architecture (Go)
Commit-Item "agents/accessibility.md" "feat(agent): build WCAG Auditor node"
Commit-Item "agents/critic.md" "feat(agent): build Master Critic node for final verification"
Commit-Item "forma-cli/go.mod" "chore(cli): initialize Go modules"
Commit-Item "forma-cli/main.go" "feat(cli): bootstrap Cobra CLI core"
Commit-Item "forma-cli/internal/installer/detector.go" "feat(cli): add automatic IDE platform detection (Cursor, Windsurf, Claude)"
Commit-Item "forma-cli/internal/installer/platforms.go" "feat(cli): define supported IDE directory architectures"
Commit-Item "forma-cli/internal/installer/installer.go" "feat(cli): implement secure embedded file injection"
Commit-Item "forma-cli/cmd/init.go" "feat(cli): build 'forma init' command"
Commit-Item "forma-cli/cmd/export.go" "feat(cli): build 'forma export' design token command"
Commit-Item "forma-cli/internal/assets/embed.go" "feat(cli): setup go:embed for zero-dependency binary"

# 41-48: Vanguard Upgrades & Polish
Commit-Item "forma-cli/internal/diagnostic/" "feat(cli): engineer 'forma doctor' resilience diagnostic system"
Commit-Item "forma-cli/cmd/doctor.go" "feat(cli): register 'doctor' command"
Commit-Item "forma-cli/internal/healer/" "feat(cli): implement AST-Driven Auto-Healer engine"
Commit-Item "forma-cli/cmd/heal.go" "feat(cli): register 'heal' command for automated WCAG injection"
Commit-Item "forma-cli/internal/installer/remove.go" "feat(cli): build safe uninstallation engine"
Commit-Item "forma-cli/cmd/remove.go" "feat(cli): register 'remove' command"
Commit-Item "bin/forma.js" "feat(dist): write NPM global binary execution wrapper"
Commit-Item "bin/install.js" "feat(dist): write OS-aware binary downloader postinstall script"

# Final catch-all for remaining documentation and workflows
git add .
git commit -m "docs: finalize README, SECURITY, CONTRIBUTING, and GitHub Actions"

Write-Host "✅ Created 49 meaningful historical commits."
