from aoc20211201a import window
from aoc20221214a import *


def aoc(data):
    w, depth = rock(parse(data))
    depth += 2
    return sand(w, depth, True)
