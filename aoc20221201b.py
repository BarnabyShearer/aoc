from aoc20221201a import *


def aoc(data):
    return sum(sorted([sum(r) for r in parse(data)])[-3:])
