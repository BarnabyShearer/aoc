def parse(data):
    data = [l.split(":")[1].split("|") for l in data.split("\n")]
    return [[[int(y) for y in x.split()] for x in l] for l in data]


def aoc(data):
    total = 0
    for a, b in parse(data):
        line = -1
        for n in a:
            if n in b:
                line += 1
        if line >= 0:
            total += 2**line
    return total
