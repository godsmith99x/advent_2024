import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from day1.day1pt1 import total_distance 

class TestTotalDistance(unittest.TestCase):
    def test_total_distance(self):
        self.assertEqual(total_distance("day1/tests/test_input.csv"), 11)

if __name__ == "__main__":
    unittest.main()