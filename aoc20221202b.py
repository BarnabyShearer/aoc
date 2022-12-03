from aoc20221202a import *


def aoc(data):
    return sum(1 + (them + out - 1) % 3 + out * 3 for them, out in parse(data))
