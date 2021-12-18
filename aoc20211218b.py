from aoc20211218a import *


def aoc(data):
    data = parse(data)
    total = 0
    for a in data:
        for b in data:
            total = max(total, magnitude(i_am_lazy(add(a, b))))
    return total
