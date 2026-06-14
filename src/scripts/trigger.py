import sys
import json
import re

class AdvancedIntentParser:
    def __init__(self):
        # Weighted intent mapping: (Agent) -> [(Pattern, Weight)]
        self.intents = {
            "architect": [
                (r"\b(build|create|generate|scaffold|init|start)\b", 1.0),
                (r"\b(design system|tokens|theme|palette|typography)\b", 1.5),
                (r"\b(project|app|website|dashboard)\b", 0.5)
            ],
            "researcher": [
                (r"\b(analyze|research|audience|users|flow|journey|ux|friction)\b", 1.5),
                (r"\b(who|why|goal|purpose)\b", 1.0)
            ],
            "psychologist": [
                (r"\b(convert|conversion|sales|growth|psychology|trust|behavior)\b", 1.5),
                (r"\b(cta|call to action|persuade|bias)\b", 1.0)
            ],
            "component": [
                (r"\b(component|button|card|modal|table|input|form|nav)\b", 1.5),
                (r"\b(state|hover|focus|anatomy|structure)\b", 1.0)
            ],
            "frontend": [
                (r"\b(code|react|vue|svelte|html|tailwind|css|nextjs|implement|build)\b", 1.5),
                (r"\b(pixel|perfect|ui|interface)\b", 0.5)
            ],
            "critic": [
                (r"\b(review|audit|check|score|grade|critique|feedback)\b", 1.5),
                (r"\b(wrong|bad|ugly|fix|improve)\b", 1.0)
            ],
            "accessibility": [
                (r"\b(a11y|accessible|wcag|contrast|screen reader|aria|blind)\b", 2.0),
                (r"\b(check|audit)\b", 0.5)
            ]
        }

        # Mandatory couplings (If A is active, B must be active)
        self.dependencies = {
            "frontend": ["component", "architect"],
            "component": ["architect"],
            "psychologist": ["researcher"],
            "critic": ["accessibility"]
        }

    def parse(self, prompt):
        prompt_lower = prompt.lower()
        scores = {agent: 0.0 for agent in self.intents}

        # 1. Calculate weighted scores
        for agent, patterns in self.intents.items():
            for pattern, weight in patterns:
                if re.search(pattern, prompt_lower):
                    scores[agent] += weight

        # 2. Determine active agents (Threshold = 1.0)
        active_agents = set([agent for agent, score in scores.items() if score >= 1.0])

        # 3. Fallback: If no intent detected, default to standard build pipeline
        if not active_agents:
            active_agents = {"architect", "researcher", "component", "frontend"}

        # 4. Resolve dependencies
        final_agents = set(active_agents)
        for agent in active_agents:
            if agent in self.dependencies:
                final_agents.update(self.dependencies[agent])

        # 5. Order execution logically
        execution_order = ["researcher", "psychologist", "architect", "component", "frontend", "critic", "accessibility"]
        ordered_agents = [agent for agent in execution_order if agent in final_agents]

        return ordered_agents

if __name__ == "__main__":
    parser = AdvancedIntentParser()
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
        active_agents = parser.parse(prompt)
        print(json.dumps(active_agents))
    else:
        print(json.dumps(["architect", "frontend"]))
