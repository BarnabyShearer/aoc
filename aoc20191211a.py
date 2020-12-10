from cpu import cpu

MAP = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def robot(data, paint={}):
    x, y, d = (0, 0, 0)
    c = cpu(data)
    try:
        while True:
            next(c)
            paint[(x, y)] = c.send(paint.get((x, y), 0))
            d += 1 if next(c) else -1
            d %= 4
            x += MAP[d][0]
            y += MAP[d][1]
    except StopIteration:
        pass
    return paint


def aoc(data):
    return len(robot(data))
