#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class BowlingScoreCalculator:
    def __init__(self):
        self._frames = None
        self._frame_idx = None
        self._frame = None

    def score_game(self, frames):
        self._frames = frames
        score = 0
        for self._frame_idx, self._frame in enumerate(frames):
            score += sum(self._frame)
            score += self._get_next_throw() if self._is_spare() else 0
        return score

    def _get_next_throw(self):
        return self._frames[self._frame_idx+1][0]

    def _is_spare(self):
        return sum(self._frame) == 10

