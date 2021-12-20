from aoc20211219a import *


def aoc(data):
    sensors, _ = slam(parse(data))
    return max(sum(abs(x) for x in sub(a, b)) for a in sensors for b in sensors)
