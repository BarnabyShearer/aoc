def slope(data, x, y):
    xi = 0
    total = 0
    for yi, line in enumerate(data.split("\n")):
        if yi % y == 0:
            if line[xi] == "#":
                total += 1
            xi += x
            xi %= len(line)
    return total


def aoc(data):
    return slope(data, 3, 1)
