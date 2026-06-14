import unittest
import sys
import os

# Add scripts directory to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))
from token_bridge import extract_value

class TestTokenBridge(unittest.TestCase):
    def test_extract_value(self):
        # Test direct extraction
        self.assertEqual(extract_value("spring"), "spring")
        
        # Test dictionary extraction (W3C standard)
        token = {"$value": "#FFFFFF", "$type": "color"}
        self.assertEqual(extract_value(token), "#FFFFFF")

if __name__ == '__main__':
    unittest.main()
