from collections import defaultdict


def parse(d):
    return [
        [[int(i) for i in c.split(",")] for c in l.split(" -> ")] for l in d.split("\n")
    ]


def count_cross(map):
    return sum(v >= 2 for v in map.values())


def along(s, e):
    d = 1 if s < e else -1
    return range(s, e + d, d)


def aoc(data):
    map = defaultdict(lambda: 0)
    for (sx, sy), (ex, ey) in parse(data):
        if sx == ex or sy == ey:
            for c in ((x, y) for y in along(sy, ey) for x in along(sx, ex)):
                map[c] += 1
    return count_cross(map)
