from aoc20211201a import window


def parse(data):
    _, __, x, y = data.split()
    x1, x2 = (int(v) for v in x[2:-1].split(".."))
    y1, y2 = (int(v) for v in y[2:].split(".."))
    return x1, x2, y1, y2


def step(dx, dy):
    x = y = 0
    while True:
        yield (x := x + dx), (y := y + dy)
        dx += dx and (-1, 1)[dx < 0]
        dy -= 1


def hits(x1, x2, y1, y2):
    for dy in range(1000, y1 - 1, -1):
        for dx in range(1, x2 + 1):
            for x, y in step(dx, dy):
                if x1 <= x <= x2 and y1 <= y <= y2:
                    yield dx, dy
                    break
                elif x > x2 or y < y1:
                    break


def zenith(steps):
    for a, b in window(steps):
        if b < a:
            return a


def aoc(data):
    return zenith(y for _, y in step(*next(hits(*parse(data)))))
