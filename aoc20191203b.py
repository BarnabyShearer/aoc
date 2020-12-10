from aoc20191203a import wire


def aoc(data):
    wires = []
    wires_dist = []
    for line in data.split("\n"):
        cords = set()
        dist = {}
        d = 0
        for x, y in wire(line):
            d += 1
            cords.add((x, y))
            if (x, y) not in dist:
                dist[(x, y)] = d
        wires.append(cords)
        wires_dist.append(dist)
    dist = set()
    for cord in wires[0] | wires[1]:
        if cord in wires[0] and cord in wires[1]:
            dist.add(wires_dist[0][cord] + wires_dist[1][cord])
    return min(dist)
