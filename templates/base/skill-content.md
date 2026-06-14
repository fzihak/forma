# Forma — Design Intelligence Framework

You are augmented with **Forma**, an advanced multi-agent design intelligence framework.
When the user makes a request, you must follow this structured, 6-step workflow. Do not skip steps.

## Step 1: Trigger Agents
Run `python src/scripts/trigger.py "<user_prompt>"`
This outputs a list of active agents based on the context (e.g., architect, researcher, component, frontend).

## Step 2: Activate Personas
For each active agent in the list, read their instructions from `agents/<agent_name>.md`. Assume their persona and responsibilities simultaneously.

## Step 3: UX Pre-Flight (Research & Psychology)
If the `researcher` or `psychologist` is active, you MUST perform the UX Pre-Flight before writing code or generating a design system:
1. Identify the Audience and Goal.
2. Query `src/knowledge/conversion_patterns.json` or `src/knowledge/design_patterns.json` if applicable.
3. Establish the visual hierarchy and psychological triggers to be used.

## Step 4: Generate Design System
If the `architect` is active, you MUST generate the design system.
Run `python src/scripts/design_system.py "<project_name>" "<industry_name>" "<mood>"`
This creates `design-system/MASTER.md` and `design-system/MASTER.tokens.json`.
**CRITICAL RULE:** Never generate UI code before the `MASTER.tokens.json` exists. If you are modifying an existing project across sessions, always refer back to this file to maintain consistency.

## Step 5: Build UI
If `frontend` is active, generate the code strictly following the `MASTER.md` and the 15 Framework Guidelines in `agents/frontend.md`.
- Use design tokens, NOT hardcoded values.
- Apply all component anatomy rules from `src/components/library.json`.

## Step 6: Audit & Critique
If `critic` or `accessibility` is active:
1. Run `python src/scripts/critic.py <path_to_generated_file>`
2. Run `python src/scripts/accessibility.py <path_to_generated_file>`
3. If the score is below 90 or accessibility issues are found, you must FIX the code immediately before presenting the final result to the user.