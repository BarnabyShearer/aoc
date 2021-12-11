CARDINAL = ((-1, 0), (1, 0), (0, -1), (0, 1))


def parse(data):
    return [[int(c) for c in r] for r in data.split("\n")]


def lget(l, x, d):
    return d if not l[x : x + 1] else l[x]


def low(data):
    for y, r in enumerate(data):
        for x, c in enumerate(r):
            if not sum(
                c >= lget(lget(data, y + dy, []), x + dx, 10) for dx, dy in CARDINAL
            ):
                yield x, y, c


def aoc(data):
    return sum(c + 1 for _, _, c in low(parse(data)))
