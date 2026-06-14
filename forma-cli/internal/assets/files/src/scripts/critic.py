import sys
import os
import re
import json
import json
import logging

class SecuritySandbox:
    @staticmethod
    def validate_path(target_path, base_workspace=None):
        """
        Advanced Path Traversal Protection.
        Ensures target_path resolves strictly within the authorized workspace.
        """
        if base_workspace is None:
            base_workspace = os.getcwd()
            
        abs_target = os.path.abspath(target_path)
        abs_base = os.path.abspath(base_workspace)
        
        # Check if the resolved target path starts with the base workspace path
        if not abs_target.startswith(abs_base):
            raise PermissionError(f"[SECURITY VIOLATION] Attempted path traversal detected. Access to '{target_path}' is forbidden.")
        return abs_target

def load_design_system():
    ds_path = os.path.join(os.getcwd(), 'design-system', 'MASTER.tokens.json')
    if os.path.exists(ds_path):
        with open(ds_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def analyze_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    score = 100
    deductions = []

    # 1. Visual Hierarchy (25pts)
    if not re.search(r'<h1.*?>', content) and not re.search(r'className=.*text-[4-9]xl', content):
        score -= 10
        deductions.append("Visual Hierarchy (-10): Missing primary h1 or equivalent large typography.")
    
    # 2. Consistency (25pts)
    # Check for hardcoded colors instead of tokens
    hardcoded_colors = re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}\b', content)
    if len(hardcoded_colors) > 3:
        score -= 15
        deductions.append(f"Consistency (-15): Found {len(hardcoded_colors)} hardcoded hex colors instead of design tokens.")

    # Check for inline styles
    inline_styles = re.findall(r'style=\{?["\']', content)
    if inline_styles:
        score -= 5
        deductions.append(f"Consistency (-5): Found {len(inline_styles)} instances of inline styles.")

    # 3. Accessibility (25pts)
    if '<img' in content and 'alt=' not in content:
        score -= 15
        deductions.append("Accessibility (-15): Found <img> tags missing alt attributes.")
    
    if '<button' in content and 'aria-label=' not in content and re.search(r'<button.*?><svg', content):
        score -= 10
        deductions.append("Accessibility (-10): Found icon buttons missing aria-labels.")

    # 4. Conversion (25pts)
    if '<button' not in content and '<a ' not in content:
        score -= 15
        deductions.append("Conversion (-15): No clear Calls to Action (buttons or links) found.")

    return score, deductions

def main():
    if len(sys.argv) < 2:
        print("Usage: python critic.py <target_file_or_directory>")
        sys.exit(1)

    target = sys.argv[1]
    
    print("\n" + "="*50)
    print(" 🔍 FORMA CRITIC ENGINE - SELF-AUDIT REPORT")
    print("="*50 + "\n")

    ds = load_design_system()
    if ds:
        print("✅ Design System constraints loaded (MASTER.tokens.json)")
    else:
        print("⚠️ No design system found. Using default heuristics.")

    if not os.path.exists(target):
        print(f"❌ Target path not found: {target}")
        sys.exit(1)

    try:
        # Enforce advanced security sandboxing
        secured_target = SecuritySandbox.validate_path(target)
    except PermissionError as e:
        print(f"🛑 {e}")
        sys.exit(1)

    total_score = 0
    files_checked = 0
    all_deductions = []

    if os.path.isfile(secured_target):
        score, deductions = analyze_file(secured_target)
        total_score += score
        files_checked += 1
        all_deductions.extend(deductions)
    else:
        for root, dirs, files in os.walk(secured_target):
            for file in files:
                if file.endswith(('.html', '.tsx', '.jsx', '.vue', '.svelte')):
                    filepath = os.path.join(root, file)
                    score, deductions = analyze_file(filepath)
                    total_score += score
                    files_checked += 1
                    all_deductions.extend([f"{file}: {d}" for d in deductions])

    if files_checked == 0:
        print("❌ No UI files found to critique (.html, .tsx, .jsx, .vue, .svelte)")
        sys.exit(1)

    avg_score = total_score / files_checked

    print(f"\n📊 AUDIT SCORE: {avg_score:.1f} / 100")
    
    if avg_score >= 90:
        print("🌟 GRADE: A (Production Ready)")
    elif avg_score >= 75:
        print("👍 GRADE: B (Needs Minor Polish)")
    else:
        print("⚠️ GRADE: C (Significant Issues - Revision Required)")

    if all_deductions:
        print("\n🛑 DEDUCTIONS & ISSUES:")
        for deduction in all_deductions:
            print(f"  - {deduction}")
    else:
        print("\n✨ Perfect Score! No deductions found.")

    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
