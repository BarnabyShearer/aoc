import re

MV = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}


def step(map, x, y, f):
    ox = x
    oy = y
    of = f
    x += MV[f][0]
    y += MV[f][1]
    if y < 0 or y == len(map) or x < 0 or x == len(map[y]) or map[y][x] == " ":
        if f == 0 and y < 50:
            x, y, f = 99, 149 - y, 2
        elif f == 0 and y < 100:
            x, y, f = 100 + y - 50, 49, 3
        elif f == 0 and y < 150:
            x, y, f = 149, 49 - (y - 100), 2
        elif f == 0:
            x, y, f = 50 + y - 150, 149, 3

        elif f == 1 and x < 50:
            x, y, f = x + 100, 0, 1
        elif f == 1 and x < 100:
            x, y, f = 49, 150 + x - 50, 2
        elif f == 1:
            x, y, f = 99, 50 + x - 100, 2

        elif f == 2 and y < 50:
            x, y, f = 0, 149 - y, 0
        elif f == 2 and y < 100:
            x, y, f = y - 50, 100, 1
        elif f == 2 and y < 150:
            x, y, f = 50, 49 - (y - 100), 0
        elif f == 2:
            x, y, f = 50 + y - 150, 0, 1

        elif f == 3 and x < 50:
            x, y, f = 50, x + 50, 0
        elif f == 3 and x < 100:
            x, y, f = 0, 150 + x - 50, 0
        elif f == 3:
            x, y, f = x - 100, 199, 3

    if map[y][x] == "#":
        return ox, oy, of

    return x, y, f


def aoc(data):
    map, inst = data.split("\n\n")
    width = map.index("\n")
    map = [(l + (" " * width))[:width] for l in map.split("\n")]
    inst = re.findall("\d+|R|L", inst)
    x, y, f = 50, 0, 0
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

    return 1000 * (y + 1) + 4 * (x + 1) + f
