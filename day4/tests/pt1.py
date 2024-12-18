import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pt1 import count_xmas_pt1

class TestCountXmasPt1(unittest.TestCase):
    def test_count_xmas_pt1a(self):
        self.assertEqual(count_xmas_pt1("day4/tests/test_input.txt"), 18)

    def test_count_xmas_pt1b(self):
        self.assertEqual(count_xmas_pt1("day4/input.txt"), 2493)
if __name__ == "__main__":
    unittest.main()