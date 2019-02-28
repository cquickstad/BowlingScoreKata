#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import unittest
from bowling_score import BowlingScoreCalculator as BSC


class MyTestCase(unittest.TestCase):
    def test_zero_score(self):
        frames = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        self.assertEqual(BSC.score_game(frames), 0)

    def test_simple_adding(self):
        self.assertEqual(BSC.score_game(((1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))),
                         1)
        self.assertEqual(BSC.score_game(((1, 2), (3, 4), (1, 0), (0, 1), (2, 2), (3, 2), (7, 0), (0, 4), (1, 8), (2, 3))),
                         46)


if __name__ == '__main__':
    unittest.main()
