from aoc20201203a import slope


def aoc(data):
    total = 1
    for x, y in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        total *= slope(data, x, y)
    return total
