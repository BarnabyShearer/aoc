import math


def parse(data):
    return [[int(v) for v in l.split()[1:]] for l in data.split("\n")]


def race(data):
    total = []
    for t, d in zip(*parse(data)):
        wins = 0
        for h in range(1, t):
            if (t - h) * h > d:
                wins += 1
        total.append(wins)
    return math.prod(total)


def aoc(data):
    return race(data)
