def spiral(steps):
    dx = 1
    dy = 0
    dd = 1
    x = 0
    y = 0
    d = 0
    for _ in range(steps - 1):
        x += dx
        y += dy
        d += 1
        if d == dd:
            d = 0
            tmp = dx
            dx = -dy
            dy = tmp
            if dy == 0:
                dd += 1
        yield x, y


def aoc(data):
    *_, (x, y) = spiral(int(data))
    return abs(x) + abs(y)
