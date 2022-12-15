from aoc20221215a import *


def aoc(data, limit=4000000):
    nope = defaultdict(lambda: set())
    for x, y, xx, yy in parse(data):
        r = abs(xx - x) + abs(yy - y)
        for yyy in range(y - r + 1, y + r):
            rx = r - abs(yyy - y)
            ds = max(0, x - rx)
            de = min(limit, x + rx)
            if de > ds:
                nope[yyy].add((ds, de))
    for y in range(limit):
        r = merge(nope[y])
        if len(r) > 1:
            return (r[0][1] + 1) * 4000000 + y
