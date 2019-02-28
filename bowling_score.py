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
        return 0 if self._is_last_frame() else self._frames[self._frame_idx+1][0]

    def _get_next_two_throws(self):
        if self._is_last_frame():
            return 0
        elif len(self._frames[self._frame_idx+1]) < 2:
            return self._frames[self._frame_idx+1][0] + self._frames[self._frame_idx+2][0]
        return sum(self._frames[self._frame_idx+1][0:2])

    def _is_last_frame(self):
        return self._frame_idx + 1 >= len(self._frames)

    def _is_strike(self):
        if len(self._frame) > 0:
            return self._frame[0] == 10
        return False

    def _is_spare(self):
        return sum(self._frame) == 10

