from aoc20211201a import *


def aoc(data):
    return count_inc(sum(w) for w in window(parse(data), 3))
