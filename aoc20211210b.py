from statistics import median
from aoc20211210a import *


def score(msg):
    total = 0
    for c in msg:
        total = total * 5 + {")": 1, "]": 2, "}": 3, ">": 4}[c]
    return total


def aoc(data):
    return median(score(m) for s, m in (p(l) for l in parse(data)) if not s)
