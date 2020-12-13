from cpu import cpu


def tractor(data, x, y):
    c = cpu(data)
    next(c)
    c.send(x)
    return c.send(y)


def aoc(data):
    total = 0
    for y in range(50):
        for x in range(50):
            t = tractor(data, x, y)
            total += t
            print("#" if t else " ", end="")
        print()
    return total
