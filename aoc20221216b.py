from collections import defaultdict
from aoc20221216a import *


def aoc(data):
    all = solve(*prep(parse(data)), 26)
    return max(all[e] + all[h] for e in all.keys() for h in all.keys() if not h & e)
