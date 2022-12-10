from aoc20221210a import *
from aoc20211213b import char


def aoc(data):
    crt = {
        (i % 40, i // 40) for i, x in enumerate(cpu(data)) if x - 1 <= i % 40 <= x + 1
    }
    return "".join(char(crt, l) for l in range(0, 40, 5))
