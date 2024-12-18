import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pt1 import uncorrupted_mul

class TestUncorruptedMul(unittest.TestCase):
    def test_uncorrupted_mul(self):
        self.assertEqual(uncorrupted_mul("day3/tests/test_input_pt1.txt"), 161)

if __name__ == "__main__":
    unittest.main()