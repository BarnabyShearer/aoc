from aoc20221223a import *


def aoc(data):
    total = 0
    elves = parse(data)
    check = [N, S, W, E]
    old_elves = set()
    while old_elves != elves:
        total += 1
        old_elves = elves
        elves, check = step(elves, check)

    return total
