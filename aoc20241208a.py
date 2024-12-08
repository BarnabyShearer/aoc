from itertools import combinations


def parse(data):
    t = {}
    w, h = 0, 0
    for y, l in enumerate(data.split("\n")):
        for x, c in enumerate(l):
            w, h = x, y
            if c != ".":
                if not c in t:
                    t[c] = set()
                t[c].add((x, y))
    return t, w + 1, h + 1


def calc(t, h):
    n = set()
    for c, v in t.items():
        for a, b in combinations(v, 2):
            for i in h:
                n.add((b[0] + (b[0] - a[0]) * i, b[1] + (b[1] - a[1]) * i))
                n.add((a[0] + (a[0] - b[0]) * i, a[1] + (a[1] - b[1]) * i))
    return n


def clean(n, w, h):
    for x, y in n.copy():
        if x < 0 or x >= w or y < 0 or y >= h:
            n.remove((x, y))
    return n


def aoc(data):
    t, w, h = parse(data)
    return len(clean(calc(t, (1,)), w, h))
