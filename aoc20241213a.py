import numpy as np


def parse(data):
    for m in data.split("\n\n"):
        yield (
            (int(ii[2:]) for ii in i.split(": ")[1].split(", ")) for i in m.split("\n")
        )


def solve(ax, ay, bx, by, mx, my):
    x = np.round(np.linalg.solve(np.array([[ax, bx], [ay, by]]), np.array([mx, my])))
    if x[0] * ax + x[1] * bx == mx and x[0] * ay + x[1] * by == my:
        return int(3 * x[0] + x[1])
    return 0


def aoc(data):
    total = 0
    for (ax, ay), (bx, by), (mx, my) in parse(data):
        total += solve(ax, ay, bx, by, mx, my)
    return total
