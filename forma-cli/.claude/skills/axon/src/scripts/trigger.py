import sys
import json

TRIGGER_KEYWORDS = {
    "build":   ["architect", "researcher", "component", "frontend"],
    "design":  ["architect", "psychologist", "component"],
    "create":  ["architect", "researcher", "component", "frontend"],
    "review":  ["critic", "accessibility"],
    "audit":   ["critic", "accessibility"],
    "fix":     ["critic", "frontend"],
    "improve": ["critic", "psychologist"]
}

def get_active_agents(prompt):
    prompt_lower = prompt.lower()
    agents = set()
    for keyword, agent_list in TRIGGER_KEYWORDS.items():
        if keyword in prompt_lower:
            agents.update(agent_list)
    return list(agents) if agents else ["architect", "frontend"]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
        active_agents = get_active_agents(prompt)
        print(json.dumps(active_agents))
    else:
        print(json.dumps(["architect", "frontend"]))
