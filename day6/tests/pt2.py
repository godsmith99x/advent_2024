import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pt2 import sum_middle_values_pt2

class TestPt2(unittest.TestCase):
    def test_sum_middle_values_pt2a(self):
        self.assertEqual(sum_middle_values_pt2("day5/tests/test_input.txt"), 123)

    def test_sum_middle_values_pt2b(self):
        self.assertEqual(sum_middle_values_pt2("day5/input.txt"), 4679)

if __name__ == "__main__":
    unittest.main()