from collections import defaultdict


def _parse(data):
    square = set()
    O = set()
    for y, l in enumerate(data.split("\n")):
        for x, c in enumerate(l):
            if y == 0:
                square.add((x, -1))
                square.add((x, len(data.split("\n"))))
            if c == "#":
                square.add((x, y))
            if c == "O":
                O.add((x, y))
        square.add((-1, y))
        square.add((len(l), y))
    return square, O


def parse(data):
    height, width = len(data.split("\n")), len(data.split("\n")[0])
    square, O = _parse(data)
    n, e, s, w = (
        {"xx": 0, "yy": 1},
        {"xx": -1, "yy": 0},
        {"xx": 0, "yy": -1},
        {"xx": 1, "yy": 0},
    )
    for (x, y) in square:
        yy = y + 1
        while (x, yy) not in square and yy < height:
            n[(x, yy)] = (x, y)
            yy += 1
        yy = y - 1
        while (x, yy) not in square and yy >= 0:
            s[(x, yy)] = (x, y)
            yy -= 1
        xx = x + 1
        while (xx, y) not in square and xx < width:
            w[(xx, y)] = (x, y)
            xx += 1
        xx = x - 1
        while (xx, y) not in square and xx >= 0:
            e[(xx, y)] = (x, y)
            xx -= 1
    return height, width, square, O, n, e, s, w


def aoc(data):
    height, width, square, O, n, e, s, w = parse(data)

    hit = defaultdict(lambda: 0)
    for o in O:
        hit[n[o]] += 1

    total = 0
    for x, y in square:
        total += sum(height - 1 - y - yy for yy in range(hit[(x, y)]))
    return total
