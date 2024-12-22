from collections import defaultdict
from aoc20211215a import CARDINAL


def a_star(data, start, dest):
    open = set((start,))
    score = defaultdict(lambda: float("inf"))
    guess = defaultdict(lambda: float("inf"))
    score[start] = guess[start] = 0
    while open:
        x, y = min(open, key=guess.get)
        if (x, y) == dest:
            return score[(x, y)]
        open.remove((x, y))
        for nx, ny in ((x + dx, y + dy) for dx, dy in CARDINAL):
            if (nx, ny) in data:
                new_score = score[(x, y)] + 1
                if new_score < score[(nx, ny)]:
                    score[(nx, ny)] = new_score
                    guess[(nx, ny)] = new_score + dest[0] - nx + dest[1] - ny
                    open.add((nx, ny))


def aoc(data):
    map = {}
    for y in range(71):
        for x in range(71):
            map[(x, y)] = 1
    for x, y in ((int(ii) for ii in i.split(",")) for i in data.split("\n")[:1024]):
        del map[(x, y)]
    return a_star(map, (0, 0), (70, 70))
