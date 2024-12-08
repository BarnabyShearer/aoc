from itertools import pairwise


def ok(v):
    dir = None
    for a, b in pairwise(v):
        if dir == None:
            dir = a < b
        if 0 < abs(a - b) <= 3:
            if (a < b) == dir:
                continue
        return False
    return True


def aoc(data):
    total = 0
    for r in data.split("\n"):
        if ok(int(i) for i in r.split()):
            total += 1
    return total
