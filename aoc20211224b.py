from aoc20211224a import *


def aoc(data):
    digits = [1] * 14
    for i, ii, offset in calc(parse(data)):
        if offset > 0:
            digits[i] += offset
        else:
            digits[ii] -= offset
    return "".join(str(d) for d in digits)
