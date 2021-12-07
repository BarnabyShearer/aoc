from aoc20211205a import *


def aoc(data):
    map = defaultdict(lambda: 0)
    for (sx, sy), (ex, ey) in parse(data):
        for x in along(sx, ex):
            if sx == ex or sy == ey:
                for y in along(sy, ey):
                    map[x, y] += 1
            else:
                d = -1 if (sx < ex) ^ (sy < ey) else 1
                map[x, sy + (x - sx) * d] += 1
    return count_cross(map)
