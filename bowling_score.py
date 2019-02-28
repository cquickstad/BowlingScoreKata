#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class BowlingScoreCalculator:
    @staticmethod
    def score_game(frames):
        n = 0
        for frame in frames:
            n += sum(frame)
        return n

