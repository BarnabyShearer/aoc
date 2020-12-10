MAP = {
    "<": (-1, 0),
    "^": (0, 1),
    ">": (1, 0),
    "v": (0, -1),
}


def visited(data):
    result = set()
    x, y = (0, 0)
    result.add((x, y))
    for dir in data:
        x += MAP[dir][0]
        y += MAP[dir][1]
        result.add((x, y))
    return result


def aoc(data):
    return len(visited(data))
