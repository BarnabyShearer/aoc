from aoc20211206a import *


def aoc(data):
    return sum(th(breed(parse(data)), 256).values())
