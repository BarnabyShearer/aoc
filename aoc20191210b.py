import math

from aoc20191210a import parse, best, asteroids


def aoc(data):
    map = parse(data)
    _, x, y = best(map)
    seen = {}
    for xx, yy in asteroids(map):
        if xx == x and yy == y:
            continue
        seen.setdefault(
            (math.atan2(yy - y, xx - x) + math.pi / 2) % (math.pi * 2), []
        ).append((xx, yy))
    for angle in seen.keys():
        seen[angle] = sorted(
            seen[angle], key=lambda ast: abs(ast[0] - x) + abs(ast[1] - y)
        )
    count = 0
    while True:
        for angle in sorted(seen.keys()):
            ast = seen[angle].pop(0)
            if ast:
                count += 1
                if count == 200:
                    return ast[0] * 100 + ast[1]
