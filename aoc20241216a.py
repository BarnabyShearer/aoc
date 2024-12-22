from collections import defaultdict


def solve(data):
    seen = defaultdict(lambda: float("inf"))
    edge = defaultdict(lambda: float("inf"))
    end = (0, 0)
    for y, l in enumerate(data):
        for x, c in enumerate(l):
            if c == "S":
                seen[(x, y, 1, 0)] = 0
                edge[(x, y, 1, 0)] = 0
            if c == "E":
                end = (x, y)
    for i in range(1000):
        oldedge = edge.copy()
        edge = {}

        for (x, y, dx, dy), s in oldedge.items():
            for xx, yy, ddx, ddy, ss in (
                (x + dx, y + dy, dx, dy, s + 1),
                (x, y, -dy, dx, s + 1000),
                (x, y, dy, -dx, s + 1000),
            ):
                if data[yy][xx] == "." or data[yy][xx] == "E":
                    if ss < seen[(xx, yy, ddx, ddy)]:
                        edge[(xx, yy, ddx, ddy)] = ss
                        seen[(xx, yy, ddx, ddy)] = ss
    return (
        seen,
        min(seen[(*end, dx, dy)] for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))),
        end,
    )


def aoc(data):
    return solve(data.split("\n"))[1]
