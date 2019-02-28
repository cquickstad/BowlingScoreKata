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

    def test_spare_adds_next_throw(self):
        frames = ((0, 0), (0, 0), (0, 0), (0, 0), (6, 4), (3, 0), (0, 0), (0, 0), (0, 0), (0, 0))
        self.assertEqual(self.cut.score_game(frames), 16)

    def test_spare_on_last_frame(self):
        frames = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 9, 7))
        self.assertEqual(self.cut.score_game(frames), 17)

        frames = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 10, 10))
        self.assertEqual(self.cut.score_game(frames), 20)

        frames = ((0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 10, 0))
        self.assertEqual(self.cut.score_game(frames), 10)


if __name__ == '__main__':
    unittest.main()
