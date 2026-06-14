import json
import os
import sys

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
        # try fallback
        data = load_json("industries/saas-general.json")
    return data

def load_psychology_triggers():
    return load_json("psychology/triggers.json")

def load_component_library():
    return load_json("components/library.json")

def build_color_system(colors_data, industry_data):
    system = {}
    if colors_data:
        for key, value in colors_data.items():
            if isinstance(value, str) and value.startswith("#"):
                slug = key.lower().replace(" ", "-")
                system[slug] = {"$value": value, "$type": "color"}
    
    if not system:
        system = {
            "primary": {"$value": "#1A73E8", "$type": "color"},
            "surface": {"$value": "#F8FAFC", "$type": "color"}
        }
    return system

def derive_radius(styles_data):
    if styles_data and "css_keywords" in styles_data:
        kw = styles_data["css_keywords"]
        if "rounded-full" in kw:
            return "9999px"
        elif "rounded-none" in kw:
            return "0px"
        elif "rounded-2xl" in kw:
            return "16px"
    return "8px"

def derive_elevation(styles_data):
    return "0 4px 6px rgba(0,0,0,0.1)"

def get_full_psychology_details(trigger_names, all_triggers):
    details = []
    if isinstance(all_triggers, list):
        for trigger in all_triggers:
            if trigger.get("name") in trigger_names:
                details.append(trigger)
    return details

def get_full_component_details(comp_names, all_comps):
    details = []
    if isinstance(all_comps, list):
        for comp in all_comps:
            if comp.get("name") in comp_names:
                details.append(comp)
    return details

def generate_design_system(project_name, industry, mood):
    industry_data = load_industry(industry)
    
    styles = search(f"{industry} {mood}", domain="ui_styles")
    colors = search(f"{industry} {mood}", domain="color_systems")
    fonts  = search(f"{industry} {mood}", domain="typography")
    
    style_data = styles[0] if styles else {}
    color_data = colors[0] if colors else {}
    font_data = fonts[0] if fonts else {}
    
    all_triggers = load_psychology_triggers()
    all_components = load_component_library()
    
    trigger_names = industry_data.get("psychology_triggers", [])
    comp_names = industry_data.get("core_components", [])
    
    active_triggers = get_full_psychology_details(trigger_names, all_triggers)
    active_components = get_full_component_details(comp_names, all_components)
    
    design_system = {
        "$schema": "https://design-tokens.org/schema.json",
        "project": project_name,
        "typography": {
            "heading": {"$value": font_data.get("Heading Font", "Inter"), "$type": "fontFamily"},
            "body": {"$value": font_data.get("Body Font", "Roboto"), "$type": "fontFamily"},
            "scale-xs": {"$value": "12px", "$type": "dimension"},
            "scale-base": {"$value": "16px", "$type": "dimension"},
            "scale-lg": {"$value": "18px", "$type": "dimension"}
        },
        "color": build_color_system(color_data, industry_data),
        "spacing": {
            "sm": {"$value": "4px", "$type": "dimension"},
            "base": {"$value": "8px", "$type": "dimension"},
            "lg": {"$value": "16px", "$type": "dimension"}
        },
        "border_radius": {"base": {"$value": derive_radius(style_data), "$type": "dimension"}},
        "elevation_rules": derive_elevation(style_data),
        "advanced_intelligence": {
            "industry_constraints": industry_data.get("industry_constraints", []),
            "forbidden_patterns": industry_data.get("forbidden_patterns", []),
            "required_patterns": industry_data.get("required_patterns", []),
            "psychology_triggers": active_triggers,
            "core_components": active_components
        }
    }
    
    out_dir = os.path.join(os.path.dirname(__file__), "..", "..", "design-system")
    os.makedirs(out_dir, exist_ok=True)
    
    with open(os.path.join(out_dir, "MASTER.tokens.json"), "w", encoding="utf-8") as f:
        json.dump(design_system, f, indent=2)
        
    with open(os.path.join(out_dir, "MASTER.md"), "w", encoding="utf-8") as f:
        f.write(f"# Design System for {project_name}\n\n")
        f.write(f"**Industry:** {industry_data.get('name', industry)}\n\n")
        
        f.write("## 🚫 Forbidden Patterns\n")
        for fp in design_system["advanced_intelligence"]["forbidden_patterns"]:
            f.write(f"- {fp}\n")
            
        f.write("\n## ✅ Required Patterns\n")
        for rp in design_system["advanced_intelligence"]["required_patterns"]:
            f.write(f"- {rp}\n")
            
        f.write("\n## 🧠 Psychology Triggers to Apply\n")
        for trigger in design_system["advanced_intelligence"]["psychology_triggers"]:
            f.write(f"### {trigger.get('name', '')}\n")
            f.write(f"- **How to Apply**: {trigger.get('how_to_apply', '')}\n")
            f.write(f"- **Anti-Pattern**: {', '.join(trigger.get('anti_patterns', []))}\n")
            
        f.write("\n## 🧩 Core Components Architecture\n")
        for comp in design_system["advanced_intelligence"]["core_components"]:
            f.write(f"### {comp.get('name', '')}\n")
            f.write(f"- **Anatomy**: {', '.join(comp.get('anatomy', []))}\n")
            f.write(f"- **Accessibility**: {', '.join(comp.get('accessibility_rules', []))}\n")
    
    return design_system

if __name__ == "__main__":
    if len(sys.argv) > 3:
        print(json.dumps(generate_design_system(sys.argv[1], sys.argv[2], sys.argv[3]), indent=2))
