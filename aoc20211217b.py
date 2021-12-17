from aoc20211217a import *


def aoc(data):
    return sum(1 for _ in hits(*parse(data)))
