from aoc20221224a import *


def aoc(data):
    storm, start, end, w, h = parse(data)
    storm, t1 = do(storm, start, end, w, h)
    storm, t2 = do(storm, end, start, w, h)
    storm, t3 = do(storm, start, end, w, h)
    return t1 + t2 + t3
