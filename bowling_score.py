#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


class BowlingScoreCalculator:
    @staticmethod
    def score(frames):
        n = 0
        for frame in frames:
            for pins in frame:
                n += pins
        return n

