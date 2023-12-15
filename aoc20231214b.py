from aoc20231214a import *


def aoc(data):
    height, width, square, O, n, e, s, w = parse(data)

    seen = {}
    states = {}
    for i in range(1000000000):
        for d in (n, w, s, e):
            hit = defaultdict(lambda: 0)
            for o in O:
                hit[d[o]] += 1
            O = set()
            for (x, y), v in hit.items():
                for r in range(1, v + 1):
                    O.add((x + r * d["xx"], y + r * d["yy"]))
            O = frozenset(O)
            if O in seen:
                hit = states[seen[O] - 1 + ((1000000000 - i) % (i - seen[O]))]
                total = 0
                for x, y in square:
                    total += (height - y) * hit[(x, y)]
                return total
            seen[O] = i
            states[i] = hit
