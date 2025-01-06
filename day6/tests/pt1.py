import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pt1 import count_guard_moves_pt1

class TestPt1(unittest.TestCase):
    def test_count_guard_moves_pt1a(self):
        self.assertEqual(count_guard_moves_pt1("day6/tests/test_input.txt"), 41)

    def test_count_guard_moves_pt1b(self):
        self.assertEqual(count_guard_moves_pt1("day6/input.txt"), 5080)

if __name__ == "__main__":
    unittest.main()