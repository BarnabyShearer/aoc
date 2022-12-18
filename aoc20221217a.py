from itertools import cycle

SHAPES = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##"""


def shapes(data):
    return [
        {
            (x, y)
            for x in range(4)
            for y in range(4)
            if f"\n\n\n{s}".split("\n")[-y - 1][x : x + 1] == "#"
        }
        for s in data.split("\n\n")
    ]


def _c(w, x, y):
    return x < 0 or x >= 7 or y < 0 or (x, y) in w


def c(w, x, y, s):
    return any(_c(w, xx + x, yy + y) for xx, yy in s)


def run(data, t):
    s, i, x, y, w = shapes(SHAPES), 0, 2, 3, set()

    for d in cycle(data):
        x += 1 if d == ">" else -1
        if c(w, x, y, s[i % len(s)]):
            x -= 1 if d == ">" else -1
        y -= 1
        if c(w, x, y, s[i % len(s)]):
            y += 1
            w.update((xx + x, yy + y) for xx, yy in s[i % len(s)])
            i += 1
            x, y = 2, max(y for x, y in w) + 4
            if i == t:
                return y - 3


def aoc(data):
    return run(data, 2022)
