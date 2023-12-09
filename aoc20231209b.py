from aoc20231209a import *


def aoc(data):
    total = 0
    for line in parse(data):
        step = 0
        for a in diffs(line)[-2::-1]:
            step = a[0] - step
        total += step
    return total
