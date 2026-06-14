import json
import sys

def tokens_to_tailwind(tokens_json):
    """W3C tokens → tailwind.config.js"""
    config = {
        "theme": {
            "colors": {},
            "fontFamily": {},
            "spacing": {}
        }
    }
    for key, value in tokens_json.get("color", {}).items():
        config["theme"]["colors"][key] = value["$value"]
    for key, value in tokens_json.get("typography", {}).items():
        config["theme"]["fontFamily"][key] = [value["$value"], "sans-serif"]
    for key, value in tokens_json.get("spacing", {}).items():
        config["theme"]["spacing"][key] = value["$value"]
    return f"module.exports = {json.dumps(config, indent=2)}"

def tokens_to_css_vars(tokens_json):
    """W3C tokens → CSS custom properties"""
    lines = [":root {"]
    for category, tokens in tokens_json.items():
        if category.startswith("$") or not isinstance(tokens, dict):
            continue
        for name, token in tokens.items():
            if isinstance(token, dict) and "$value" in token:
                lines.append(f"  --{category}-{name}: {token['$value']};")
    lines.append("}")
    return "\n".join(lines)

def tokens_to_scss(tokens_json):
    """W3C tokens → SCSS variables"""
    lines = []
    for category, tokens in tokens_json.items():
        if category.startswith("$") or not isinstance(tokens, dict):
            continue
        for name, token in tokens.items():
            if isinstance(token, dict) and "$value" in token:
                lines.append(f"${category}-{name}: {token['$value']};")
    return "\n".join(lines)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        fmt = sys.argv[1]
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            tokens = json.load(f)
            if fmt == "tailwind":
                print(tokens_to_tailwind(tokens))
            elif fmt == "css-vars":
                print(tokens_to_css_vars(tokens))
            elif fmt == "scss":
                print(tokens_to_scss(tokens))
