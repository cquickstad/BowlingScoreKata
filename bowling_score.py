#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class BowlingScoreCalculator:
    def __init__(self):
        self._frame = None

    def score_game(self, frames):
        score = 0
        for i, self._frame in enumerate(frames):
            score += sum(self._frame)
            if sum(self._frame) == 10:  # spare
                score += frames[i+1][0]
        return score

