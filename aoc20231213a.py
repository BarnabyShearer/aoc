def parse(data):
    return (d.split("\n") for d in data.split("\n\n"))


def reflect(p):
    for y in range(len(p) - 1):
        if all(p[y - yy] == p[y + yy + 1] for yy in range(min(y + 1, len(p) - y - 1))):
            yield y + 1


def aoc(data):
    total = 0
    for p in parse(data):
        for a in reflect(p):
            total += 100 * a
        for b in reflect(tuple("".join(c) for c in zip(*p))):
            total += b
    return total
