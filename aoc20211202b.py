from aoc20211202a import *


def aoc(data):
    x = y = aim = 0
    for dx, dy in parse(data):
        x += dx
        y += aim * dx
        aim += dy
    return x * y
