import unittest
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from day1.pt2 import similarity_score 

class TestSimilarityScore(unittest.TestCase):
    def test_similarity_score(self):
        self.assertEqual(similarity_score("day1/tests/test_input.csv"), 31)

if __name__ == "__main__":
    unittest.main()