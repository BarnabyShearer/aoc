from collections import defaultdict


def match(t, d):
    total = 0
    open = {tt: 0 for tt in t}
    while open:
        n = defaultdict(lambda: 0)
        for tt in open:
            if d == tt:
                total += open[d]
            elif d.startswith(tt):
                for ttt in t:
                    n[tt + ttt] += open[tt] or 1
        open = n
    return total


def aoc(data):
    t, d = data.split("\n\n")
    t = t.split(", ")
    d = d.split("\n")
    total = 0
    for dd in d:
        if match(t, dd) > 0:
            total += 1
    return total
