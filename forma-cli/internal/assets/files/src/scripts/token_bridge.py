import json
import sys

def extract_value(token):
    if isinstance(token, dict) and "$value" in token:
        return token["$value"]
    return str(token)

def tokens_to_tailwind(tokens_json):
    """W3C tokens → Advanced tailwind.config.js"""
    config = {
        "theme": {
            "extend": {
                "colors": {},
                "fontFamily": {},
                "spacing": {},
                "borderRadius": {},
                "transitionDuration": {},
                "transitionTimingFunction": {}
            }
        }
    }
    
    for key, value in tokens_json.get("color", {}).items():
        config["theme"]["extend"]["colors"][key] = extract_value(value)
        
    for key, value in tokens_json.get("typography", {}).items():
        if key in ["heading", "body", "mono"]:
            config["theme"]["extend"]["fontFamily"][key] = [extract_value(value), "sans-serif"]
            
    for key, value in tokens_json.get("spacing", {}).items():
        config["theme"]["extend"]["spacing"][key] = extract_value(value)
        
    for key, value in tokens_json.get("border_radius", {}).items():
        config["theme"]["extend"]["borderRadius"][key] = extract_value(value)
        
    for key, value in tokens_json.get("animation", {}).items():
        if key.endswith("-duration"):
            name = key.replace("-duration", "")
            config["theme"]["extend"]["transitionDuration"][name] = extract_value(value)
        elif key.endswith("-easing"):
            name = key.replace("-easing", "")
            config["theme"]["extend"]["transitionTimingFunction"][name] = extract_value(value)
        elif key.endswith("-type"):
            name = key.replace("-type", "")
            if "animation" not in config["theme"]["extend"]:
                config["theme"]["extend"]["animation"] = {}
            # Register basic animation name placeholder for physics/apis
            config["theme"]["extend"]["animation"][name] = extract_value(value)
        elif key.endswith("-stiffness") or key.endswith("-damping") or key.endswith("-mass"):
            if "springPhysics" not in config["theme"]["extend"]:
                config["theme"]["extend"]["springPhysics"] = {}
            config["theme"]["extend"]["springPhysics"][key] = extract_value(value)

    return f"/** @type {{import('tailwindcss').Config}} */\nmodule.exports = {json.dumps(config, indent=2)}"

def tokens_to_css_vars(tokens_json):
    """W3C tokens → Advanced CSS custom properties"""
    lines = [":root {"]
    for category, tokens in tokens_json.items():
        if category.startswith("$") or not isinstance(tokens, dict):
            continue
        for name, token in tokens.items():
            val = extract_value(token)
            # Filter out complex nested dicts that weren't parsed
            if not isinstance(val, dict):
                lines.append(f"  --{category}-{name}: {val};")
    lines.append("}")
    return "\n".join(lines)

def tokens_to_scss(tokens_json):
    """W3C tokens → Advanced SCSS variables"""
    lines = []
    for category, tokens in tokens_json.items():
        if category.startswith("$") or not isinstance(tokens, dict):
            continue
        for name, token in tokens.items():
            val = extract_value(token)
            if not isinstance(val, dict):
                lines.append(f"${category}-{name}: {val};")
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
