from aoc20241218a import a_star


def aoc(data):
    map = {}
    for y in range(71):
        for x in range(71):
            map[(x, y)] = 1
    for x, y in ((int(ii) for ii in i.split(",")) for i in data.split("\n")):
        del map[(x, y)]
        if a_star(map, (0, 0), (70, 70)) is None:
            return ",".join((x, y))
