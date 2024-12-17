import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pt1 import count_safe_reports_pt1

class TestCountSafeReports(unittest.TestCase):
    def test_count_safe_reports(self):
        self.assertEqual(count_safe_reports_pt1("day2/tests/test_input.csv"), 2)

if __name__ == "__main__":
    unittest.main()