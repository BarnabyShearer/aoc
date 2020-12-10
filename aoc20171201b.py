from aoc20171201a import same


def aoc(data):
    return sum(same([int(d) for d in data], len(data) // 2))
