from aoc20241211a import do


def aoc(data):
    total = 0
    for c in [int(i) for i in data.split()]:
        total += do(c, 75)
    return total
