def parse(data):
    return [int(x) for x in data.split(",")]


def moves(data, cost=lambda c: c):
    for target in range(min(data), max(data)):
        yield sum(cost(abs(d - target)) for d in data)


def aoc(data):
    return min(moves(parse(data)))
