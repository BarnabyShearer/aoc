import math


def parse(data):
    return [[c == "#" for c in l] for l in data.split("\n")]


def asteroids(map):
    for y, line in enumerate(map):
        for x, v in enumerate(line):
            if v:
                yield x, y


def best(map):
    best = (0, 0, 0)
    for x, y in asteroids(map):
        seen = set()
        for xx, yy in asteroids(map):
            if xx == x and yy == y:
                continue
            seen.add(math.atan2(yy - y, xx - x))
        if len(seen) > best[0]:
            best = [len(seen), x, y]
    return best


def aoc(data):
    return best(parse(data))[0]
