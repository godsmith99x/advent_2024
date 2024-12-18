import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pt2 import count_xmas_pt2

class TestCountXmasPt1(unittest.TestCase):
    def test_count_xmas_pt2a(self):
        self.assertEqual(count_xmas_pt2("day4/tests/test_input.txt"), 9)

    def test_count_xmas_pt2b(self):
        self.assertEqual(count_xmas_pt2("day4/input.txt"), 1890)
if __name__ == "__main__":
    unittest.main()