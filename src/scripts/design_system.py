import json
import os
import sys
import html

# To support being called from CLI
sys.path.insert(0, os.path.dirname(__file__))
from search import search

def load_json(rel_path):
    path = os.path.join(os.path.dirname(__file__), "..", rel_path)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}

def load_industry(industry):
    data = load_json(f"industries/{industry}.json")
    if not data:
        data = load_json("industries/saas-general.json")
    return data

def build_advanced_color_system(colors_data, industry_data):
    system = {}
    if colors_data:
        # Expected advanced structure handling
        for key, value in colors_data.items():
            if isinstance(value, str) and value.startswith("#"):
                slug = key.lower().replace(" ", "-")
                system[slug] = {"$value": value, "$type": "color"}
            elif isinstance(value, dict) and "$value" in value:
                system[key] = value

    if not system:
        # Ultimate fallback with semantic layers
        system = {
            "primary": {"$value": "#1A73E8", "$type": "color"},
            "primary-foreground": {"$value": "#FFFFFF", "$type": "color"},
            "surface": {"$value": "#F8FAFC", "$type": "color"},
            "surface-foreground": {"$value": "#0F172A", "$type": "color"},
            "destructive": {"$value": "#EF4444", "$type": "color"},
            "muted": {"$value": "#F1F5F9", "$type": "color"}
        }
    return system

def build_spacing_system():
    # Load the advanced 8-pt grid system we created earlier
    spacing_data = load_json("knowledge/spacing_systems.json")
    system = {}
    
    if spacing_data and "scale" in spacing_data:
        for item in spacing_data["scale"]:
            token = item["token"]
            if token != "none":
                system[token] = {
                    "$value": item["rem"], 
                    "$type": "dimension",
                    "pixel_equiv": item["value"],
                    "use_cases": item.get("use_cases", [])
                }
    else:
        # Fallback if file missing
        system = {
            "sm": {"$value": "0.25rem", "$type": "dimension"},
            "base": {"$value": "1rem", "$type": "dimension"},
            "lg": {"$value": "1.5rem", "$type": "dimension"}
        }
    return system

def build_interaction_system():
    # Load advanced physics and modern APIs
    interactions = load_json("knowledge/interaction_patterns.json")
    system = {}
    
    if isinstance(interactions, list):
        for interaction in interactions:
            slug = interaction.get("name", "").lower().replace(" ", "-").replace("/", "-").replace("(", "").replace(")", "")
            if "timing" in interaction:
                timing = interaction["timing"]
                if "type" in timing:
                    system[f"{slug}-type"] = {"$value": timing["type"], "$type": "string"}
                if "stiffness" in timing:
                    system[f"{slug}-stiffness"] = {"$value": timing["stiffness"], "$type": "number"}
                if "damping" in timing:
                    system[f"{slug}-damping"] = {"$value": timing["damping"], "$type": "number"}
                if "mass" in timing:
                    system[f"{slug}-mass"] = {"$value": timing["mass"], "$type": "number"}
                if "duration" in timing:
                    system[f"{slug}-duration"] = {"$value": timing["duration"], "$type": "duration"}
                if "easing" in timing:
                    system[f"{slug}-easing"] = {"$value": timing["easing"], "$type": "cubic-bezier"}
    return system

def build_typography_system(font_data):
    # Base font families from search
    system = {
        "heading": {"$value": font_data.get("Heading Font", "Inter"), "$type": "fontFamily"},
        "body": {"$value": font_data.get("Body Font", "Roboto"), "$type": "fontFamily"}
    }
    
    # Fluid typography scales from knowledge
    fluid_typo = load_json("knowledge/typography.json")
    if fluid_typo and "scale" in fluid_typo:
        for item in fluid_typo["scale"]:
            system[item["token"]] = {
                "$value": item["size"],
                "$type": "dimension",
                "line_height": item.get("line_height", "1.5")
            }
    else:
        # Fallback
        system["scale-base"] = {"$value": "1rem", "$type": "dimension"}
        
    return system

def generate_design_system(project_name, industry, mood):
    project_name = html.escape(project_name)
    industry = html.escape(industry)
    mood = html.escape(mood)

    industry_data = load_industry(industry)
    
    # Semantic Search Engine Integration
    styles = search(f"{industry} {mood}", domain="ui_styles")
    colors = search(f"{industry} {mood}", domain="color_systems")
    fonts  = search(f"{industry} {mood}", domain="typography")
    
    style_data = styles[0] if styles else {}
    color_data = colors[0] if colors else {}
    font_data = fonts[0] if fonts else {}
    
    design_system = {
        "$schema": "https://design-tokens.org/schema.json",
        "project": project_name,
        "typography": build_typography_system(font_data),
        "color": build_advanced_color_system(color_data, industry_data),
        "spacing": build_spacing_system(),
        "animation": build_interaction_system(),
        "border_radius": {
            "sm": {"$value": "0.125rem", "$type": "dimension"},
            "base": {"$value": "0.375rem", "$type": "dimension"},
            "lg": {"$value": "0.5rem", "$type": "dimension"},
            "full": {"$value": "9999px", "$type": "dimension"}
        },
        "advanced_intelligence": {
            "industry_constraints": industry_data.get("industry_constraints", []),
            "forbidden_patterns": industry_data.get("forbidden_patterns", []),
            "required_patterns": industry_data.get("required_patterns", []),
            "psychology_triggers": industry_data.get("psychology_triggers", []),
            "core_components": industry_data.get("core_components", [])
        }
    }
    
    out_dir = os.path.join(os.path.dirname(__file__), "..", "..", "design-system")
    os.makedirs(out_dir, exist_ok=True)
    
    with open(os.path.join(out_dir, "MASTER.tokens.json"), "w", encoding="utf-8") as f:
        json.dump(design_system, f, indent=2)
        
    with open(os.path.join(out_dir, "MASTER.md"), "w", encoding="utf-8") as f:
        f.write(f"# Advanced Design System for {project_name}\n\n")
        f.write(f"**Industry Context:** {industry_data.get('name', industry)}\n\n")
        
        f.write("## 🚫 Strict Forbidden Patterns\n")
        for fp in design_system["advanced_intelligence"]["forbidden_patterns"]:
            f.write(f"- [FATAL] {fp}\n")
            
        f.write("\n## ✅ Mandatory Architectural Patterns\n")
        for rp in design_system["advanced_intelligence"]["required_patterns"]:
            f.write(f"- [REQUIRED] {rp}\n")
            
        f.write("\n## 🧠 Active Psychology Triggers\n")
        for trigger in design_system["advanced_intelligence"]["psychology_triggers"]:
            f.write(f"- {trigger}\n")
            
        f.write("\n## 🧩 Baseline Component Anatomy\n")
        for comp in design_system["advanced_intelligence"]["core_components"]:
            f.write(f"- {comp}\n")
            
        f.write("\n---\n*Generated by Forma Prime Architect Node. Do not edit tokens manually.*")
    
    return design_system

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print(json.dumps(generate_design_system(sys.argv[1], sys.argv[2], sys.argv[3]), indent=2))
