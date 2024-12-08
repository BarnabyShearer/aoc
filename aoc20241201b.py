from aoc20241201a import parse


def aoc(data):
    a, b = parse(data)
    return sum(aa * b.count(aa) for aa in a)
