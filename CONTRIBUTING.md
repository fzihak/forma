# Contributing to Forma

First off, thank you for considering contributing to Forma! It's people like you that make Forma such a powerful and versatile Design Intelligence Framework.

## Project Structure

Forma is split into two primary components:
1. **The Intelligence Engine** (`/src`): Built with Python and JSON. This handles the design system generation, OKLCH math, typography scales, and W3C token bridges.
2. **The Command Line Interface** (`/forma-cli`): Built with Go. This is the ultra-fast wrapper that installs the AI skills, runs the AST Auto-Healer, and performs system diagnostics.

## Development Setup

### Requirements
- Node.js 18+ (For NPM wrapping)
- Python 3.9+ (For the intelligence engine)
- Go 1.22+ (For the CLI)

### 1. Cloning & Testing Locally
When developing, you don't need to build the NPM package every time. You can run the Go source directly.

```bash
git clone https://github.com/fzihak/forma.git
cd forma/forma-cli

# Test the installer without downloading binaries (use local source)
go run main.go init --ai claude --offline
```

### 2. Running the Test Suite
Before submitting any pull requests, you must ensure both the Go and Python test suites pass:

```bash
# Run Go Auto-Healer tests
cd forma-cli
go test ./internal/healer/...

# Run Python Engine tests
cd ..
python -m unittest src/tests/test_engine.py
```

## Adding New Knowledge

If you want to add new Design Styles, Industry Profiles, or Psychology Triggers, you do not need to write Go or Python code. Simply edit the JSON files in the `src/` directory.

- `src/knowledge/color_systems.json`: Add new OKLCH palettes.
- `src/industries/`: Add a new `.json` file for a new industry profile.
- `src/components/`: Add a new `.json` file for component blueprints.

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a build.
2. Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.
3. You may merge the Pull Request in once you have the sign-off of at least one other developer, or if you do not have permission to do that, you may request the reviewer to merge it for you.

## License
By contributing, you agree that your contributions will be licensed under its MIT License.
