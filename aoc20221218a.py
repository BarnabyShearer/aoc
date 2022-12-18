SIDE = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)


def add(a, b):
    return tuple(c + d for c, d in zip(a, b))


def parse(data):
    return {tuple(int(i) for i in l.split(",")) for l in data.split("\n")}


def surface(data):
    return sum(1 for d in data for s in SIDE if add(d, s) not in data)


def aoc(data):
    return surface(parse(data))
