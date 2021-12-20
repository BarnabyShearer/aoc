from aoc20211220a import *


def aoc(data):
    kernel, i = parse(data)
    inverted = False
    for _ in range(50):
        i, inverted = enhance(kernel, i, inverted)
    return len(i)
