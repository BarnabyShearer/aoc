PIPES = {
    "|": ((0, -1), (0, 1)),
    "-": ((-1, 0), (1, 0)),
    "L": ((0, -1), (1, 0)),
    "J": ((0, -1), (-1, 0)),
    "7": ((0, 1), (-1, 0)),
    "F": ((0, 1), (1, 0)),
}


def parse(data):
    data = data.split("\n")
    start = None
    map = {}
    for y, l in enumerate(data):
        for x, c in enumerate(l):
            if c == ".":
                continue
            if c == "S":
                start = (x, y)
                continue
            map[(x, y)] = tuple(((x + xx), (y + yy)) for xx, yy in PIPES[c])

    for k, ((xx, yy), (xxx, yyy)) in PIPES.items():
        if start in map.get((start[0] + xx, start[1] + yy), []) and start in map.get(
            (start[0] + xxx, start[1] + yyy), []
        ):
            map[start] = (
                (start[0] + xx, start[1] + yy),
                (start[0] + xxx, start[1] + yyy),
            )
            data[start[1]] = (
                data[start[1]][: start[0]] + k + data[start[1]][start[0] + 1 :]
            )

    loop = set((start,))
    prev, pos = start, map[start][0]
    while pos != start:
        loop.add(pos)
        pos_next = map[pos][0] if map[pos][0] != prev else map[pos][1]
        prev = pos
        pos = pos_next
    return data, start, loop


def aoc(data):
    _, start, loop = parse(data)
    return int(len(loop) / 2)
