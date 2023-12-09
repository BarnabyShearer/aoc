from itertools import pairwise


def parse(data):
    return [[int(d) for d in l.split()] for l in data.split("\n")]


def diffs(line):
    all = [line]
    while all[-1][-1] != 0:
        all.append([b - a for a, b in pairwise(all[-1])])
    return all


def aoc(data):
    return sum(sum(a[-1] for a in diffs(line)[-2::-1]) for line in parse(data))
