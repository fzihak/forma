import sys
import os
import json
import logging
from bs4 import BeautifulSoup
import re

class SecuritySandbox:
    @staticmethod
    def validate_path(target_path, base_workspace=None):
        if base_workspace is None:
            base_workspace = os.getcwd()
            
        abs_target = os.path.abspath(target_path)
        abs_base = os.path.abspath(base_workspace)
        
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

    # Use BeautifulSoup to parse the AST. For JSX/TSX, 'html.parser' handles nested elements well enough.
    soup = BeautifulSoup(content, 'html.parser')

    # 1. Visual Hierarchy (25pts)
    h1_tags = soup.find_all(['h1'])
    large_text_regex = re.compile(r'text-[4-9]xl|text-\d+px')
    has_large_text = False
    for tag in soup.find_all(True):
        classes = tag.get('class')
        if classes:
            class_str = ' '.join(classes) if isinstance(classes, list) else classes
            if large_text_regex.search(class_str):
                has_large_text = True
                break
    
    if not h1_tags and not has_large_text:
        score -= 10
        deductions.append("Visual Hierarchy (-10): Missing primary h1 or equivalent large typography.")

    # 2. Consistency (25pts)
    inline_styles = soup.find_all(style=True)
    if inline_styles:
        score -= 5
        deductions.append(f"Consistency (-5): Found {len(inline_styles)} instances of inline styles.")

    hardcoded_colors = re.findall(r'#(?:[0-9a-fA-F]{3}){1,2}\b', content)
    if len(hardcoded_colors) > 3:
        score -= 15
        deductions.append(f"Consistency (-15): Found {len(hardcoded_colors)} hardcoded hex colors instead of design tokens.")

    # 3. Accessibility (25pts)
    images = soup.find_all('img')
    missing_alts = [img for img in images if not img.has_attr('alt')]
    if missing_alts:
        score -= 15
        deductions.append(f"Accessibility (-15): Found {len(missing_alts)} <img> tags missing alt attributes.")

    buttons = soup.find_all('button')
    missing_aria_buttons = []
    for btn in buttons:
        has_text = len(btn.get_text(strip=True)) > 0
        has_svg = btn.find('svg') is not None
        if not has_text and has_svg and not btn.has_attr('aria-label') and not btn.has_attr('aria-labelledby'):
            missing_aria_buttons.append(btn)
            
    if missing_aria_buttons:
        score -= 10
        deductions.append(f"Accessibility (-10): Found {len(missing_aria_buttons)} icon buttons missing aria-labels.")

    # 4. Conversion (25pts)
    links = soup.find_all('a')
    if not buttons and not links:
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
