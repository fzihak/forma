import sys
import os
import re
import json
import logging

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

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    if len(hex_code) == 3:
        hex_code = ''.join([c*2 for c in hex_code])
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

def relative_luminance(rgb):
    # Calculate WCAG relative luminance
    rs = [c / 255.0 for c in rgb]
    ls = []
    for r in rs:
        if r <= 0.03928:
            ls.append(r / 12.92)
        else:
            ls.append(((r + 0.055) / 1.055) ** 2.4)
    return 0.2126 * ls[0] + 0.7152 * ls[1] + 0.0722 * ls[2]

def contrast_ratio(hex1, hex2):
    try:
        rgb1 = hex_to_rgb(hex1)
        rgb2 = hex_to_rgb(hex2)
    except ValueError:
        return 0.0

    l1 = relative_luminance(rgb1)
    l2 = relative_luminance(rgb2)
    
    lighter = max(l1, l2)
    darker = min(l1, l2)
    
    return (lighter + 0.05) / (darker + 0.05)

def analyze_touch_targets(content):
    issues = []
    # Simplified check: looking for small height/width classes in buttons
    small_targets = re.findall(r'<button[^>]*class="[^"]*\b([hw]-[1-6])\b[^"]*"', content)
    if small_targets:
        issues.append(f"Found {len(small_targets)} buttons with potentially small touch targets (e.g. h-4, w-6). Recommended minimum is 44x44px.")
    return issues

def main():
    if len(sys.argv) >= 3:
        # Direct contrast check
        color1 = sys.argv[1]
        color2 = sys.argv[2]
        ratio = contrast_ratio(color1, color2)
        print(f"\n🎨 CONTRAST CHECK: {color1} vs {color2}")
        print(f"Ratio: {ratio:.2f}:1")
        
        if ratio >= 7.0:
            print("✅ WCAG AAA Compliant (Normal Text)")
        elif ratio >= 4.5:
            print("✅ WCAG AA Compliant (Normal Text) / AAA (Large Text)")
        elif ratio >= 3.0:
            print("⚠️ WCAG AA Compliant (Large Text / UI Components Only)")
        else:
            print("❌ Fails WCAG accessibility standards")
        sys.exit(0)
        
    elif len(sys.argv) == 2:
        # File/Directory scan
        target = sys.argv[1]
        print("\n" + "="*50)
        print(" ♿ FORMA ACCESSIBILITY ENGINE - SCAN REPORT")
        print("="*50 + "\n")
        
        if not os.path.exists(target):
            print(f"❌ Target path not found: {target}")
            sys.exit(1)

        try:
            secured_target = SecuritySandbox.validate_path(target)
        except PermissionError as e:
            print(f"🛑 {e}")
            sys.exit(1)
            
        issues = []
        if os.path.isfile(secured_target):
            with open(secured_target, 'r', encoding='utf-8') as f:
                content = f.read()
                issues.extend(analyze_touch_targets(content))
        
        if issues:
            print("🛑 ACCESSIBILITY ISSUES FOUND:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("✨ Basic accessibility checks passed.")
            
        print("\nNote: Automated checks only catch ~30% of a11y issues. Manual keyboard & screen reader testing is required.")
        print("="*50 + "\n")
    else:
        print("Usage:")
        print("  Check contrast: python accessibility.py <hex1> <hex2>")
        print("  Scan file:      python accessibility.py <file_path>")
        sys.exit(1)

if __name__ == "__main__":
    main()
