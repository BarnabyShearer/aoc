from aoc20211209a import *
from math import prod


def basin(x, y, data):
    b = set()
    nb = {(x, y)}
    while nb:
        b.update(nb)
        nnb = set()
        for x, y in nb:
            for dx, dy in CARDINAL:
                if (
                    lget(lget(data, y + dy, []), x + dx, 9) != 9
                    and data[y][x] < data[y + dy][x + dx]
                ):
                    nnb.add((x + dx, y + dy))
        nb = nnb - b
    return len(b)


def aoc(data):
    data = parse(data)
    return prod(sorted(basin(x, y, data) for x, y, _ in low(data))[-3:])
