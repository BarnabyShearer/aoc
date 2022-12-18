from aoc20221218a import *
from itertools import product


def aoc(data):
    drop = parse(data)
    inv = set(product(*[range(-1, 21)] * 3)) - drop
    open = [(0, 0, 0)]
    while open:
        o = open.pop()
        if o in inv:
            inv.remove(o)
            open.extend(add(o, s) for s in SIDE)
    return surface(drop | inv)
