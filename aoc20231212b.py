from aoc20231212a import *


def aoc(data):
    total = 0
    lines, groups = parse(data)

    groups = [g * 5 for g in groups]
    lines = ["?".join([line] * 5) for line in lines]

    for line, group in zip(lines, groups):
        total += split(0, group, "", line)

    return total
