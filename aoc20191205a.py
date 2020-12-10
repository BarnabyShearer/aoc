from cpu import cpu


def aoc(data):
    c = cpu(data)
    next(c)
    c.send(1)
    return list(c)[-1]
