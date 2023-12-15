from aoc20231210a import *
from itertools import pairwise

PIPES = {
    "|": ((0, -1), (0, 1)),
    "-": ((-1, 0), (1, 0)),
    "L": ((0, -1), (1, 0)),
    "J": ((0, -1), (-1, 0)),
    "7": ((0, 1), (-1, 0)),
    "F": ((0, 1), (1, 0)),
}


def aoc(data):
    data, start, loop = parse(data)
    height, width = len(data), len(data[0])

    small = []
    for y in range(height):
        small.append("")
        for x in range(width):
            small[-1] += data[y][x] if (x, y) in loop else "."
    med = []
    for y in small:
        new_y = ""
        for x, xx in pairwise(y):
            if x == ".":
                new_y += ".."
            else:
                if xx == ".":
                    new_y += x + "."
                else:
                    if x in "-LF":
                        new_y += x + "-"
                    else:
                        new_y += x + "."
        new_y += xx
        med.append(new_y)
    big = []
    for y, yy in pairwise(med):
        new_y = ""
        for x, xx in zip(y, yy):
            if x == ".":
                new_y += "."
            else:
                if y == ".":
                    new_y += "."
                else:
                    if x in "|F7":
                        new_y += "|"
                    else:
                        new_y += "."
        big.append(y)
        big.append(new_y)
    big.append(yy)

    outer = set()

    for y in range(len(big)):
        outer.add((-1, y))
        outer.add((len(big[0]), y))
    for x in range(len(big[0])):
        outer.add((x, -1))
        outer.add((x, len(big)))

    for _ in range(100):
        for y in range(len(big)):
            for x in range(len(big[0])):
                if big[y][x] != "." or (x, y) in outer:
                    continue
                for yyy in (-1, 0, 1):
                    for xxx in (-1, 0, 1):
                        if yyy == 0 and xxx == 0:
                            continue
                        if (x + xxx, y + yyy) in outer:
                            outer.add((x, y))
    total = 0
    for y, l in enumerate(big):
        if y % 2 != 0:
            continue
        for x, c in enumerate(l):
            if x % 2 != 0:
                continue
            if (x, y) not in outer and c == ".":
                total += 1
    return total
