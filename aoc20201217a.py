from itertools import product


def nspace(d):
    return tuple(m for m in product(*((-1, 0, 1),) * d) if any(m))


def parse(data, d):
    bugs = {}
    for y, line in enumerate(data.split()):
        for x, c in enumerate(line):
            if c == "#":
                bugs[(x, y) + (0,) * (d - 2)] = True
    return bugs


def area(min, max, d):
    return product(*(range(min, max + 1),) * d)


def life(data, d):
    bugs = parse(data, d)
    space = nspace(d)
    for i in range(6):
        newbugs = {}
        for pos in area(-i - 1, 8 + i, d):
            s = sum(tuple(a + b for a, b in zip(pos, delta)) in bugs for delta in space)
            if s == 3 or pos in bugs and s == 2:
                newbugs[pos] = True
        bugs = newbugs
    return len(bugs)


def aoc(data):
    return life(data, 3)
