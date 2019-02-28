#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import unittest
from bowling_score import BowlingScoreCalculator as BSC


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.cut = BSC()

    def test_zero_score(self):
        frames = ((),)
        self.assertEqual(self.cut.score_game(frames), 0)

    def test_simple_adding(self):
        frames = ((1, 0),)
        self.assertEqual(self.cut.score_game(frames), 1)

        frames = ((1, 2), (3, 4), (1, 0), (0, 1), (2, 2), (3, 2), (7, 0), (0, 4), (1, 8), (2, 3))
        self.assertEqual(self.cut.score_game(frames), 46)

    def test_spare_adds_next_throw(self):
        frames = ((6, 4), (3, 0))
        self.assertEqual(self.cut.score_game(frames), 16)

    def test_spare_on_last_frame(self):
        frames = ((1, 9, 7),)
        self.assertEqual(self.cut.score_game(frames), 17)

        frames = ((0, 10, 10),)
        self.assertEqual(self.cut.score_game(frames), 20)

        frames = ((0, 10, 0),)
        self.assertEqual(self.cut.score_game(frames), 10)

    def test_strike_adds_next_two_throws(self):
        frames = ((10,), (3, 6))
        self.assertEqual(self.cut.score_game(frames), 28)

    def test_strike_on_last_frame(self):
        frames = ((10,), (10, 10, 10))
        self.assertEqual(self.cut.score_game(frames), 60)

    def test_perfect_game(self):
        frames = ((10,), (10,), (10,), (10,), (10,), (10,), (10,), (10,), (10,), (10, 10, 10))
        self.assertEqual(self.cut.score_game(frames), 300)

    def test_all_frames_nine_and_miss(self):
        frames = ((9,), (9,), (9,), (9,), (9,), (9,), (9,), (9,), (9,), (9,))
        self.assertEqual(self.cut.score_game(frames), 90)

    def test_all_spares_with_final_throw(self):
        frames = ((5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5), (5, 5, 5))
        self.assertEqual(self.cut.score_game(frames), 150)


if __name__ == '__main__':
    unittest.main()
