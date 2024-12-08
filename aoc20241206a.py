from aoc20241204a import g

TURN = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}


def solve(data):
    dx, dy = 0, -1
    for y, l in enumerate(data):
        for x, c in enumerate(l):
            if c == "^":
                break
        else:
            continue
        break
    seen = set()
    isloop = set()
    while x >= 0 and x < len(data[0]) and y >= 0 and y < len(data):
        if g(g(data, y + dy), x + dx) == "#":
            dx, dy = TURN[(dx, dy)]
        else:
            if (x, y, dx, dy) in isloop:
                return False
            isloop.add((x, y, dx, dy))
            seen.add((x, y))
            x += dx
            y += dy
    return seen


def aoc(data):
    data = [list(l) for l in data.split("\n")]
    return len(solve(data))
