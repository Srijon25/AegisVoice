# tests/test_evaluator.py

import unittest
from aegisvoice.evaluator import PhraseEvaluator

class TestPhraseEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = PhraseEvaluator(cancel_phrases=["abort mission", "terminate program"])

    def test_exact_match_trigger(self):
        self.assertTrue(self.evaluator.is_triggered("abort mission"))

    def test_no_match(self):
        self.assertFalse(self.evaluator.is_triggered("continue operation"))

    def test_similarity_match(self):
        # "abort the mission" is similar to "abort mission"
        # Simulate expected fuzzy match behavior
        score = self.evaluator.get_score("abort the mission")
        self.assertGreater(score, 0.75)

if __name__ == '__main__':
    unittest.main()
