from collections import defaultdict


def parse(data):
    return (
        (int(i[2:-1]) for i in (l + ",").split() if "=" in i) for l in data.split("\n")
    )


def merge(ranges):
    merged = []
    for s, e in sorted(ranges, key=lambda r: r[0]):
        if not merged or merged[-1][1] < s:
            merged.append((s, e))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
    return merged


def aoc(data, ty=2000000):
    nope = defaultdict(lambda: set())
    nopenope = defaultdict(lambda: set())
    for x, y, xx, yy in parse(data):
        nopenope[y].add(x)
        nopenope[yy].add(xx)
        r = abs(xx - x) + abs(yy - y)
        for yyy in range(y - r + 1, y + r):
            rx = r - abs(yyy - y)
            nope[yyy].add((x - rx, x + rx))
    return sum(1 + e - s for s, e in merge(nope[ty])) - len(nopenope[ty])
