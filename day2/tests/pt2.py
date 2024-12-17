import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pt2 import count_safe_reports_pt2 

class TestCountSafeReports(unittest.TestCase):
    def test_count_safe_reports(self):
        self.assertEqual(count_safe_reports_pt2("day2/tests/test_input.csv"), 4)

if __name__ == "__main__":
    unittest.main()