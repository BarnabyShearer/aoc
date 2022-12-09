from aoc20221208a import *


def score(data, x, y):
    e, w, s, n = 0, 0, 0, 0
    for e in range(1, len(data[y]) - x):
        if data[y][x + e] >= data[y][x]:
            break
    for w in range(1, x + 1):
        if data[y][x - w] >= data[y][x]:
            break
    for s in range(1, len(data) - y):
        if data[y + s][x] >= data[y][x]:
            break
    for n in range(1, y + 1):
        if data[y - n][x] >= data[y][x]:
            break
    return e * w * s * n


def aoc(data):
    data = parse(data)
    return max(score(data, x, y) for y in range(len(data)) for x in range(len(data[y])))
