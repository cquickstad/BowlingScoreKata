#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import unittest
from bowling_score import BowlingScoreCalculator as BSC


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.cut = BSC()

    def test_zero_score(self):
        frames = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        self.assertEqual(self.cut.score_game(frames), 0)

    def test_simple_adding(self):
        frames = ((1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        self.assertEqual(self.cut.score_game(frames), 1)

        frames = ((1, 2), (3, 4), (1, 0), (0, 1), (2, 2), (3, 2), (7, 0), (0, 4), (1, 8), (2, 3))
        self.assertEqual(self.cut.score_game(frames), 46)


if __name__ == '__main__':
    unittest.main()
