from aoc20211215a import *


def enbiggen(data):
    big = {}
    mx, my = max(data.keys())
    mx += 1
    my += 1
    for y in range(5 * mx):
        for x in range(5 * my):
            big[(x, y)] = ((data[(x % mx, y % my)] + y // my + x // mx) - 1) % 9 + 1
    return big


def aoc(data):
    data = enbiggen(parse(data))
    return a_star(data, (0, 0), max(data.keys()))
