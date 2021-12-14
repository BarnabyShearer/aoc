from aoc20211214a import *


def aoc(data):
    code, pairs = parse(data)
    for _ in range(40):
        code = polymerize(code, pairs)
    return score(code)
