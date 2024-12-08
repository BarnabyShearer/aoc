from aoc20241205a import parse


def good(order, l):
    for a, b in order:
        if a in l and b in l:
            if l.index(a) > l.index(b):
                return tuple(
                    l[: l.index(b)]
                    + tuple([a])
                    + l[l.index(b) + 1 : l.index(a)]
                    + tuple([b])
                    + l[l.index(a) + 1 :]
                )
    else:
        return l


def aoc(data):
    order, data = parse(data)
    total = 0
    for l in data:
        for a, b in order:
            if a in l and b in l:
                if l.index(a) > l.index(b):
                    g = good(order, tuple(l))
                    while True:
                        gg = good(order, g)
                        if g == gg:
                            break
                        g = gg
                    total += int(g[(len(g) - 1) // 2])
                    break
    return total
