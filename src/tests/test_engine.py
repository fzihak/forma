import unittest
import sys
import os
import tempfile

# Add scripts directory to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))
from token_bridge import extract_value
from critic import analyze_file

class TestTokenBridge(unittest.TestCase):
    def test_extract_value(self):
        # Test direct extraction
        self.assertEqual(extract_value("spring"), "spring")
        
        # Test dictionary extraction (W3C standard)
        token = {"$value": "#FFFFFF", "$type": "color"}
        self.assertEqual(extract_value(token), "#FFFFFF")

class TestCriticEngine(unittest.TestCase):
    def test_analyze_file_flawless(self):
        content = """
        <h1 class="text-5xl">Welcome</h1>
        <button aria-label="Submit">
            <svg></svg>
        </button>
        <img src="logo.png" alt="Logo" />
        <a href="/login">Login</a>
        """
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.html', encoding='utf-8') as f:
            f.write(content)
            temp_path = f.name
        
        try:
            score, deductions = analyze_file(temp_path)
            self.assertEqual(score, 100, f"Expected 100 but got {score}. Deductions: {deductions}")
            self.assertEqual(len(deductions), 0)
        finally:
            os.remove(temp_path)

    def test_analyze_file_broken(self):
        content = """
        <div>
            <button><svg></svg></button>
            <img src="logo.png" />
            <div style="color: #ffffff;">Hardcoded</div>
            <div style="color: #000000;">Hardcoded</div>
            <div style="color: #111111;">Hardcoded</div>
            <div style="color: #222222;">Hardcoded</div>
        </div>
        """
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.html', encoding='utf-8') as f:
            f.write(content)
            temp_path = f.name
            
        try:
            score, deductions = analyze_file(temp_path)
            self.assertTrue(score < 100)
            self.assertTrue(any("Missing primary h1" in d for d in deductions))
            self.assertTrue(any("missing alt" in d for d in deductions))
            self.assertTrue(any("missing aria-labels" in d for d in deductions))
            self.assertTrue(any("inline styles" in d for d in deductions))
            self.assertTrue(any("hardcoded hex" in d for d in deductions))
        finally:
            os.remove(temp_path)

if __name__ == '__main__':
    unittest.main()
