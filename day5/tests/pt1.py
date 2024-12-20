import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pt1 import sum_middle_values_pt1

class TestPt1(unittest.TestCase):
    def test_sum_middle_values_pt1a(self):
        self.assertEqual(sum_middle_values_pt1("day5/tests/test_input.txt"), 143)

    def test_sum_middle_values_pt1b(self):
        self.assertEqual(sum_middle_values_pt1("day5/input.txt"), 5166)

if __name__ == "__main__":
    unittest.main()