from collections import defaultdict
from aoc20231203a import *


def aoc(data):
    total = 0
    data = get_parts(data)
    data = list(filter(lambda x: x[0] == "*", data))
    counts = defaultdict(lambda: 0)
    for _, x, y, _ in data:
        counts[(x, y)] += 1
    for (x, y), v in counts.items():
        if v != 2:
            continue
        a, b = 0, 0
        for _, xx, yy, n in data:
            if xx == x and yy == y:
                a = b
                b = n
        total += a * b
    return total
