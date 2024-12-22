from aoc20241213a import parse, solve


def aoc(data):
    total = 0
    for (ax, ay), (bx, by), (mx, my) in parse(data):
        total += solve(ax, ay, bx, by, mx + 10000000000000, my + 10000000000000)
    return total
