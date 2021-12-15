from collections import defaultdict
from math import inf

CARDINAL = ((-1, 0), (1, 0), (0, -1), (0, 1))


def parse(data):
    return {(x, y): int(v) for y, r in enumerate(data.split()) for x, v in enumerate(r)}


def a_star(weight, start, dest):
    open = set((start,))
    score = defaultdict(lambda: inf)
    guess = defaultdict(lambda: inf)
    score[start] = guess[start] = 0
    while open:
        x, y = min(open, key=guess.get)
        if (x, y) == dest:
            return score[(x, y)]
        open.remove((x, y))
        for nx, ny in ((x + dx, y + dy) for dx, dy in CARDINAL):
            if (nx, ny) in weight:
                new_score = score[(x, y)] + weight[(nx, ny)]
                if new_score < score[(nx, ny)]:
                    score[(nx, ny)] = new_score
                    # Use manhatten distance to dest as heuristic
                    guess[(nx, ny)] = new_score + dest[0] - nx + dest[1] - ny
                    open.add((nx, ny))


def aoc(data):
    data = parse(data)
    return a_star(data, (0, 0), max(data.keys()))
