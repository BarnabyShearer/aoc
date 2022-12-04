from aoc20221204a import *


def aoc(data):
    return sum(1 for a, b in parse(data) if a.intersection(b))
