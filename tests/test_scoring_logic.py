import unittest
from src.scoring_logic import define_scoring_rules, calculate_scores

class TestScoringLogic(unittest.TestCase):

    def setUp(self):
        # Set up any necessary variables or configurations for the tests
        self.piece_distribution = {'red': 3, 'blue': 2, 'green': 1}
        self.heights = [1, 2, 3]
        self.detected_pieces = [
            {'color': 'red', 'height': 1},
            {'color': 'red', 'height': 2},
            {'color': 'red', 'height': 3},
            {'color': 'blue', 'height': 1},
            {'color': 'blue', 'height': 2},
            {'color': 'green', 'height': 1}
        ]

    def test_define_scoring_rules(self):
        # Test the define scoring rules function
        score = define_scoring_rules(self.piece_distribution, self.heights)
        self.assertEqual(score, 60, "Scoring rules calculation is incorrect.")

    def test_calculate_scores(self):
        # Test the calculate scores function
        score = calculate_scores(self.detected_pieces)
        self.assertEqual(score, 60, "Score calculation is incorrect.")

if __name__ == "__main__":
    unittest.main()
