import os
import json

def expand_trigger(trigger_name):
    return {
        "name": trigger_name,
        "implementation_mandate": f"Enforce {trigger_name} prominently in the main user flow.",
        "anti_pattern": f"Ignoring {trigger_name} leads to high drop-off rates in this specific industry."
    }

def expand_constraint(constraint_text):
    return {
        "constraint": constraint_text,
        "severity": "CRITICAL",
        "reasoning": "Industry standard compliance and user expectation alignment."
    }

def expand_forbidden(pattern_text):
    return {
        "pattern": pattern_text,
        "alternative": "Use established, highly-accessible atomic patterns instead."
    }

def expand_required(pattern_text):
    return {
        "pattern": pattern_text,
        "context": "Must be implemented flawlessly in the primary view/onboarding."
    }

def upgrade_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Skip if already upgraded
    if "a11y_overrides" in data:
        return

    upgraded = {
        "name": data.get("name", "Unknown Industry"),
        "description": data.get("description", "Advanced industry profile."),
        "psychology_triggers": [expand_trigger(t) for t in data.get("psychology_triggers", [])],
        "industry_constraints": [expand_constraint(c) for c in data.get("industry_constraints", [])],
        "forbidden_patterns": [expand_forbidden(p) for p in data.get("forbidden_patterns", [])],
        "required_patterns": [expand_required(p) for p in data.get("required_patterns", [])],
        "core_components": data.get("core_components", []),
        "a11y_overrides": {
            "contrast_minimum": "7.0:1 (AAA)" if "finance" in data.get("name", "").lower() or "medical" in data.get("name", "").lower() else "4.5:1 (AA)",
            "focus_ring_offset": "4px",
            "touch_target_minimum": "48px" if "mobile" in data.get("description", "").lower() else "44px"
        },
        "cognitive_load_thresholds": {
            "max_choices_per_view": 4 if "luxury" in data.get("name", "").lower() else 7,
            "max_steps_per_form": 3
        }
    }
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(upgraded, f, indent=2)

def main():
    target_dir = os.path.join(os.path.dirname(__file__), "..", "industries")
    if not os.path.exists(target_dir):
        print("Industries folder not found.")
        return
        
    count = 0
    for file in os.listdir(target_dir):
        if file.endswith(".json"):
            filepath = os.path.join(target_dir, file)
            try:
                upgrade_file(filepath)
                count += 1
            except Exception as e:
                print(f"Failed to upgrade {file}: {e}")
                
    print(f"Successfully upgraded {count} industry JSON profiles to ultra-advanced structures.")

if __name__ == "__main__":
    main()
