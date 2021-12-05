from operator import eq, ne
from aoc20211203a import *


def filter(data, op):
    for bit in range(11, -1, -1):
        data = [v for v in data if op(v & 1 << bit, most_common_bit(data, bit))]
        if len(data) == 1:
            return data[0]


def aoc(data):
    data = parse(data)
    return filter(data, eq) * filter(data, ne)
