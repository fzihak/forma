import os
import subprocess
import json

BASE_DIR = r"e:\projects\Forma"
SCRIPTS_DIR = os.path.join(BASE_DIR, "src", "scripts")

def run_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=BASE_DIR, shell=True)
    return result.stdout.strip()

def run_test(project_name, industry, mood, prompt):
    print(f"\n--- Testing Scenario: {project_name} ---")
    
    # 1. Trigger agents
    agents_output = run_cmd(f'python "{os.path.join(SCRIPTS_DIR, "trigger.py")}" "{prompt}"')
    print(f"Active Agents: {agents_output}")
    
    # 2. Generate Design System
    print("Generating Design System...")
    ds_output = run_cmd(f'python "{os.path.join(SCRIPTS_DIR, "design_system.py")}" "{project_name}" "{industry}" "{mood}"')
    
    # Verify outputs
    tokens_path = os.path.join(BASE_DIR, "design-system", "MASTER.tokens.json")
    md_path = os.path.join(BASE_DIR, "design-system", "MASTER.md")
    
    if os.path.exists(tokens_path) and os.path.exists(md_path):
        print("[SUCCESS] MASTER.tokens.json and MASTER.md created.")
        
        # 3. Generate Tailwind Config via Token Bridge
        print("Generating Tailwind Config...")
        tailwind_output = run_cmd(f'python "{os.path.join(SCRIPTS_DIR, "token_bridge.py")}" "tailwind" "{tokens_path}"')
        
        with open(os.path.join(BASE_DIR, "design-system", "tailwind.config.js"), "w", encoding="utf-8") as f:
            f.write(tailwind_output)
        print("[SUCCESS] tailwind.config.js created.")
        print("Skipping MASTER.md preview to avoid Windows encoding errors.")
    else:
        print("[ERROR] Failed to create design system files.")

def main():
    print("Starting AI Design Architect End-to-End Test Suite...")
    
    run_test(
        "Aura Finance", 
        "fintech-crypto", 
        "secure modern dark", 
        "build a crypto portfolio dashboard"
    )
    
    run_test(
        "Math Monsters", 
        "kids-learning-abc-math", 
        "playful vibrant", 
        "design a math learning game for kids"
    )
    
    run_test(
        "TaskFlow Pro", 
        "saas-general", 
        "clean minimal professional", 
        "create a new b2b task management sidebar"
    )

if __name__ == "__main__":
    main()
