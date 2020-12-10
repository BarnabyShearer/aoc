from aoc20181203a import parse


def aoc(data):
    cloth = {}
    for _, [x, y], [dx, dy] in [parse(cut) for cut in data.split("\n")]:
        for ddx in range(dx):
            for ddy in range(dy):
                cloth[(x + ddx, y + ddy)] = cloth.get((x + ddx, y + ddy), 0) + 1
    for id, [x, y], [dx, dy] in [parse(cut) for cut in data.split("\n")]:
        good = True
        for ddx in range(dx):
            for ddy in range(dy):
                if cloth[(x + ddx, y + ddy)] != 1:
                    good = False
        if good:
            return id
