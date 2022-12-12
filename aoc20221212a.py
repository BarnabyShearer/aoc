from collections import defaultdict
from math import inf
from aoc20211215a import CARDINAL


def parse(data):
    data = list(data)
    start, end, w = data.index("S"), data.index("E"), data.index("\n") + 1
    data[start], data[end] = "a", "z"
    data = "".join(data)
    start = (start % w, start // w)
    end = (end % w, end // w)
    return (
        {
            (x, y): ord(v) - ord("a")
            for y, r in enumerate(data.split())
            for x, v in enumerate(r)
        },
        start,
        end,
    )


def a_star(data, start, dest):
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
            if (nx, ny) in data and data[(nx, ny)] <= data[(x, y)] + 1:
                new_score = score[(x, y)] + 1
                if new_score < score[(nx, ny)]:
                    score[(nx, ny)] = new_score
                    # Use manhatten distance and hight to dest as heuristic
                    guess[(nx, ny)] = (
                        new_score
                        + dest[0]
                        - nx
                        + dest[1]
                        - ny
                        + data[dest]
                        - data[(nx, ny)]
                    )
                    open.add((nx, ny))


def aoc(data):
    return a_star(*parse(data))
