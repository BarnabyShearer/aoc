from aoc20221212a import *


def aoc(data):
    paths = set()
    data, _, end = parse(data)
    for k in data.keys():
        if not data[k]:
            paths.add(a_star(data, k, end) or inf)
    return min(paths)
