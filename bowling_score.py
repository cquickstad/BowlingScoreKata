#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class BowlingScoreCalculator:
    def __init__(self):
        self._frame = None

    def score_game(self, frames):
        score = 0
        for self._frame in frames:
            score += sum(self._frame)
        return score

