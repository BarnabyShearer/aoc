MOVE = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1),
}


def sign(n):
    return 1 if n > 0 else -1 if n < 0 else 0


def parse(data):
    return (MOVE[l[0]] for l in data.split("\n") for _ in range(int(l.split()[1])))


def follow(hx, hy, tx, ty):
    if abs(hx - tx) > 1 or abs(hy - ty) > 1:
        tx += sign(hx - tx)
        ty += sign(hy - ty)
    return tx, ty


def aoc(data, l=2):
    visited = set()
    rx, ry = [0] * l, [0] * l
    for x, y in parse(data):
        rx[0] += x
        ry[0] += y
        for i in range(1, l):
            rx[i], ry[i] = follow(rx[i - 1], ry[i - 1], rx[i], ry[i])
        visited.add((rx[-1], ry[-1]))
    return len(visited)
