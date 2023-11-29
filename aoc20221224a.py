MOVES = {(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)}


def parse(data):
    data = data.split("\n")
    storm = set()
    start = (data[0].index(".") - 1, -1)
    end = (data[-1].index(".") - 1, len(data) - 2)
    w = len(data[0]) - 2
    h = len(data) - 2
    for y, ll in enumerate(data):
        for x, c in enumerate(ll):
            if data[y][x] in "^v<>":
                storm.add((x - 1, y - 1, data[y][x]))
    return storm, start, end, w, h


def do(storm, start, end, w, h):
    search = [start]
    t = 0
    while search:
        next = set()
        for x, y, d in storm:
            y += {"^": -1, "v": 1, "<": 0, ">": 0}[d]
            x += {"^": 0, "v": 0, "<": -1, ">": 1}[d]
            y %= h
            x %= w
            next.add((x, y, d))
        storm = next

        curr = {(x + xx, y + yy) for x, y in search for xx, yy in MOVES}
        search = []
        t += 1

        for (x, y) in curr:
            if (x, y) == end:
                return storm, t
            if (x, y) in (start, end):
                search += [(x, y)]
            elif all((x, y, d) not in storm for d in "^v<>") and (
                x % w == x and y % h == y
            ):
                search += [(x, y)]


def aoc(data):
    return do(*parse(data))[1]
