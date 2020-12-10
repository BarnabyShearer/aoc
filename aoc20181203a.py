def parse(line):
    id, __, pos, size = line.split()
    return (
        id[1:],
        [int(x) for x in pos[:-1].split(",")],
        [int(x) for x in size.split("x")],
    )


def aoc(data):
    cloth = {}
    for _, [x, y], [dx, dy] in [parse(cut) for cut in data.split("\n")]:
        for ddx in range(dx):
            for ddy in range(dy):
                cloth[(x + ddx, y + ddy)] = cloth.get((x + ddx, y + ddy), 0) + 1
    total = 0
    for cord in cloth.values():
        if cord > 1:
            total += 1
    return total
