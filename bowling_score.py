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
            if self._is_strike():
                score += self._get_next_two_throws()
            elif self._is_spare():
                score += self._get_next_throw()
        return score

    def _get_next_throw(self):
        if self._frame_idx + 1 < len(self._frames):
            return self._frames[self._frame_idx+1][0]
        return 0

    def _get_next_two_throws(self):
        return sum(self._frames[self._frame_idx+1])

    def _is_strike(self):
        if len(self._frame) > 0:
            return self._frame[0] == 10
        return False

    def _is_spare(self):
        return sum(self._frame) == 10

