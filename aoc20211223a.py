from math import inf
from copy import copy

MOVES = (
    (3, 2, 2, 4, 6, 8, 9),
    (5, 4, 2, 2, 4, 6, 7),
    (7, 6, 4, 2, 2, 4, 5),
    (9, 8, 6, 4, 2, 2, 3),
)


def parse(data):
    data = data.split("\n")
    state = {}
    for x in range(4):
        for y in range(2, len(data)):
            if data[y][x * 2 + 3] not in ".#":
                state[(x, y - 2)] = ord(data[y][x * 2 + 3]) - ord("A")
    for h in range(7):
        hh = h * 2
        if hh == 0:
            hh = 1
        if hh == 12:
            hh = 11
        if data[1][hh] != ".":
            state[h] = ord(data[1][hh]) - ord("A")
    state[-1] = len(data) - 3
    return state


def score(a, h, x, y):
    return (10 ** a) * (MOVES[x][h] + y)


def drop(data, h, x):
    for y in range(data[-1] - 1, -1, -1):
        if (x, y) not in data:
            break
    data[(x, y)] = data[h]
    del data[h]
    return score(x, h, x, y)


def lift(data, h, x):
    for y in range(data[-1]):
        if (x, y) in data:
            break
    data[h] = data[(x, y)]
    del data[(x, y)]
    return score(data[h], h, x, y)


def game(data, score):
    for _ in range(7):
        for x in range(4):
            for y in range(data[-1] - 1, -1, -1):
                if (x, y) in data and data[(x, y)] != x:
                    break
            else:
                for h in range(x + 1, -1, -1):
                    if h not in data:
                        continue
                    if data[h] != x:
                        break
                    score += drop(data, h, x)
                for h in range(x + 2, 7):
                    if h not in data:
                        continue
                    if data[h] != x:
                        break
                    score += drop(data, h, x)

    if data == {-1: data[-1], **{(x, y): x for y in range(data[-1]) for x in range(4)}}:
        return score
    min_score = inf
    for x in range(4):
        for y in range(data[-1]):
            if (x, y) in data and data[(x, y)] != x:
                break
        else:
            continue
        for h in range(x + 1, -1, -1):
            if h in data:
                break
            newdata = copy(data)
            newscore = score + lift(newdata, h, x)
            min_score = min(min_score, game(newdata, newscore))
        for h in range(x + 2, 7):
            if h in data:
                break
            newdata = copy(data)
            newscore = score + lift(newdata, h, x)
            min_score = min(min_score, game(newdata, newscore))
    return min_score


def aoc(data):
    return game(parse(data), 0)
