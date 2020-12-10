from aoc20161201a import steps


def aoc(data):
    seen = set([(0, 0)])
    for (x, y) in steps(data):
        if (x, y) in seen:
            return abs(x) + abs(y)
        seen.add((x, y))
