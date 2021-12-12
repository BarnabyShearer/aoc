from aoc20211211a import *


def aoc(data):
    data = parse(data)
    for i in range(1000):
        data, flash = step(data, 0)
        if flash == 100:
            break
    return i + 1
