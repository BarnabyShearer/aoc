def parse(data):
    return [[int(c) for c in r.split("\n")] for r in data.split("\n\n")]


def aoc(data):
    return max([sum(r) for r in parse(data)])
