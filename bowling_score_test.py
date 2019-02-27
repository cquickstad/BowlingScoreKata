import unittest
from bowling_score import BowlingScoreCalculator as BSC


class MyTestCase(unittest.TestCase):
    def test_zero_score(self):
        frames = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        self.assertEqual(BSC.score(frames), 0)


if __name__ == '__main__':
    unittest.main()
