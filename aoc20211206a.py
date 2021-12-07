from collections import Counter
from itertools import islice


def parse(data):
    return [int(f) for f in data.split(",")]


def breed(d):
    d = Counter(d)
    while True:
        yield (d := {k: d[0] + d[7] if k == 6 else d[(k + 1) % 9] for k in range(9)})


def th(i, n):
    return next(islice(i, n - 1, None))


def aoc(data):
    return sum(th(breed(parse(data)), 80).values())
