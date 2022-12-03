from itertools import islice
from aoc20221203a import *


def chunk(l, n):
    l = iter(l)
    return iter(lambda: tuple(islice(l, n)), ())


def parse(data):
    yield from chunk(data.split("\n"), 3)


def aoc(data):
    return sum(score((set(a) & set(b) & set(c)).pop()) for a, b, c in parse(data))
