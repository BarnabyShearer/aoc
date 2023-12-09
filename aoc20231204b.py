from aoc20231204a import *


def aoc(data):
    total = 0
    wins = {}
    for c, (a, b) in list(enumerate(parse(data)))[::-1]:
        total += 1
        line = 0
        for n in a:
            if n in b:
                line += 1
        wins[c] = sum([[c + x, *wins.get(c + x, [])] for x in range(1, line + 1)], [])
        for x in wins[c]:
            total += 1
    return total
