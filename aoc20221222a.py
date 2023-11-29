import re

MV = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}


def step(map, x, y, f, ox=None, oy=None):
    if ox == None:
        ox = x
    if oy == None:
        oy = y
    x += MV[f][0]
    y += MV[f][1]
    x %= len(map[0])
    y %= len(map)
    if map[y][x] == " ":
        x, y, f = step(map, x, y, f, ox, oy)
    if map[y][x] == "#":
        return ox, oy, f
    return x, y, f


def aoc(data):
    map, inst = data.split("\n\n")
    width = map.index("\n")
    map = [(l + (" " * width))[:width] for l in map.split("\n")]
    inst = re.findall("\d+|R|L", inst)
    x = y = f = 0
    x, y, f = step(map, x, y, f)
    for i in inst:
        if i == "R":
            f += 1
            f %= 4
        elif i == "L":
            f -= 1
            f %= 4
        else:
            for _ in range(int(i)):
                x, y, f = step(map, x, y, f)

    print(x, y, f)
    return 1000 * (y + 1) + 4 * (x + 1) + f
