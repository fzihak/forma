import sys
import os
import json
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def load_json(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def detect_industry(prompt):
    prompt_lower = prompt.lower()
    if "finance" in prompt_lower or "bank" in prompt_lower or "payment" in prompt_lower or "fintech" in prompt_lower:
        return "fintech"
    if "health" in prompt_lower or "medical" in prompt_lower or "doctor" in prompt_lower:
        return "healthcare"
    if "game" in prompt_lower or "gaming" in prompt_lower or "web3" in prompt_lower:
        return "gaming"
    if "saas" in prompt_lower or "dashboard" in prompt_lower or "b2b" in prompt_lower:
        return "saas"
    if "biohack" in prompt_lower or "longevity" in prompt_lower:
        return "biohacking"
    return "general"

def generate_mandate(prompt):
    industry = detect_industry(prompt)
    
    # Load industry data
    base_dir = os.path.dirname(os.path.dirname(__file__))
    industry_path = os.path.join(base_dir, "industries", f"{industry}-app.json")
    if not os.path.exists(industry_path):
        industry_path = os.path.join(base_dir, "industries", f"{industry}.json")
        
    industry_data = load_json(industry_path)
    
    triggers = industry_data.get("psychology_triggers", [])
    constraints = industry_data.get("industry_constraints", [])
    forbidden = industry_data.get("forbidden_patterns", [])

    print(f"## 🎯 Forma Agentic Mandate: {industry.upper()} Context")
    print(f"**Original Request:** \"{prompt}\"")
    print("\n### 🧠 Psychological Triggers to Enforce")
    if triggers:
        for t in triggers[:2]:
            if isinstance(t, dict):
                print(f"- **{t.get('name', 'Trigger')}**: {t.get('implementation_mandate', '')}")
            else:
                print(f"- {t}")
    else:
        print("- Employ standard progressive disclosure (Hick's Law).")

    print("\n### 🛡️ Strict UX Constraints")
    if constraints:
        for c in constraints[:2]:
            if isinstance(c, dict):
                print(f"- **{c.get('severity', 'HIGH')}**: {c.get('constraint', '')}")
            else:
                print(f"- {c}")
    else:
        print("- Ensure AAA contrast and 48px touch targets.")

    print("\n### 🚫 Forbidden Patterns (DO NOT USE)")
    if forbidden:
        for f in forbidden[:2]:
            if isinstance(f, dict):
                print(f"- [FATAL] {f.get('pattern', '')}. Use: {f.get('alternative', '')}")
            else:
                print(f"- [FATAL] {f}")
    else:
        print("- No pure black (#000000) or pure white (#FFFFFF).")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Provide a user prompt.")
        sys.exit(1)
    generate_mandate(sys.argv[1])
