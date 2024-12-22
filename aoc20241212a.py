from aoc20241204a import g

SEEN = set()


def flood(data, c, x, y):
    if g(g(data, y), x) == c:
        if (x, y) in SEEN:
            return 0, 0
        SEEN.add((x, y))
        edge, area = 0, 1
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            if g(g(data, y + dy), x + dx) != c:
                edge += 1
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            de, da = flood(data, c, x + dx, y + dy)
            edge += de
            area += da
        return edge, area
    return 0, 0


def aoc(data):
    data = data.split("\n")
    total = 0
    for y, l in enumerate(data):
        for x, c in enumerate(l):
            de, da = flood(data, c, x, y)
            total += de * da
    return total
