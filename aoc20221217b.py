from aoc20221217a import *


def run(d, t):
    s, i, x, y, w, h, di = shapes(SHAPES), 0, 2, 3, set(), 0, 0
    cache, start = {}, (frozenset(), 0, 0, 0)
    while True:
        x += 1 if d[di % len(d)] == ">" else -1
        if c(w, x, y, s[i % len(s)]):
            x -= 1 if d[di % len(d)] == ">" else -1
        di += 1
        y -= 1
        if c(w, x, y, s[i % len(s)]):
            y += 1
            w.update((xx + x, yy + y) for xx, yy in s[i % len(s)])
            for yy in range(y, y + 3):
                if all((xx, yy) in w for xx in range(7)):
                    h += yy
                    w = {(xxx, yyy - yy) for xxx, yyy in w if yyy - yy >= 0}
                    key = (frozenset(w), i % len(s), di % len(d))
                    while key in cache and i + cache[key][0] <= t:
                        i += cache[key][0]
                        w = set(cache[key][1])
                        h += cache[key][2]
                        di = cache[key][3]
                        key2 = (frozenset(w), i % len(s), di % len(d))
                        if key == key2:
                            n = (t - i) // cache[key][0]
                            i += cache[key][0] * n
                            h += cache[key][2] * n
                        key = key2
                    cache[(start[0], start[1] % len(s), start[2])] = (
                        i - start[1],
                        key[0],
                        h - start[3],
                        key[2],
                    )
                    start = (key[0], i, key[2], h)
            i += 1
            x, y = 2, max(y for x, y in w) + 4
            if i == t:
                return h + y - 3


def aoc(data):
    return run(data, 1000000000000)
