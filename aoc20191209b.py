from cpu import cpu


def aoc(data):
    c = cpu(data)
    next(c)
    return c.send(2)
