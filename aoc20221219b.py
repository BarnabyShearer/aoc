from aoc20221219a import *
from math import prod


def aoc(data):
    return prod(brute(blueprint, 32) for blueprint in parse(data)[:3])
