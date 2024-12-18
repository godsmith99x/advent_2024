import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pt2 import uncorrupted_mul_enabled

class TestUncorruptedMulEnabled(unittest.TestCase):
    def test_uncorrupted_mul_enabled(self):
        self.assertEqual(uncorrupted_mul_enabled("day3/tests/test_input_pt2.txt"), 48)

if __name__ == "__main__":
    unittest.main()