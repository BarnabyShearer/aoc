MAP = {
    "ne": (1, 3),
    "e": (2, 0),
    "se": (1, -3),
    "sw": (-1, -3),
    "w": (-2, 0),
    "nw": (-1, 3),
}


def parse(line):
    while line != []:
        c, *line = line
        if c in "ns":
            o, *line = line
            c += o
        yield MAP[c]


def tiles(data):
    tiles = {}
    for move in data.split("\n"):
        x, y = 0, 0
        for dx, dy in parse(move):
            x += dx
            y += dy
        if (x, y) in tiles:
            del tiles[(x, y)]
        else:
            tiles[(x, y)] = True
    return tiles


def aoc(data):
    return len(tiles(data))
