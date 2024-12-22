from aoc20211215a import CARDINAL
from collections import defaultdict


def score(data, start):
    open = set((start,))
    score = defaultdict(lambda: float("inf"))
    score[start] = 0
    while open:
        x, y = open.pop()
        for nx, ny in ((x + dx, y + dy) for dx, dy in CARDINAL):
            if (nx, ny) in data:
                new_score = score[(x, y)] + 1
                if new_score < score[(nx, ny)]:
                    score[(nx, ny)] = new_score
                    open.add((nx, ny))
    return score


def run(data, cheat):
    data = data.split("\n")
    start, end = (0, 0), (0, 0)
    map = set()
    wall = set()
    for y, l in enumerate(data):
        for x, c in enumerate(l):
            if c != "#":
                map.add((x, y))
            else:
                if x > 0 and y > 0 and x < len(l) - 1 and y < len(data) - 1:
                    wall.add((x, y))
            if c == "E":
                end = (x, y)
            if c == "S":
                start = (x, y)
    forward = score(map, start)
    backwards = score(map, end)
    no_cheat = forward[end]
    total = 0

    for e1 in map:
        for e2 in map:
            if e1 == e2:
                continue
            c = abs(e1[0] - e2[0]) + abs(e1[1] - e2[1])
            if c > cheat:
                continue
            if forward[e1] + c + backwards[e2] <= no_cheat - 100:
                total += 1
    return total


def aoc(data):
    return run(data, 2)
