from aoc20241207a import solve


def aoc(data):
    return solve(data, lambda a, b: (a + b, a * b, int(str(a) + str(b))))
