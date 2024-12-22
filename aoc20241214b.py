from aoc20241214a import parse


def aoc(data):
    mx, my = 101, 103
    bots = list(parse(data))
    for t in range(1, 10000):
        for bot in bots:
            bot[0][0] += bot[1][0]
            bot[0][0] %= mx
            bot[0][1] += bot[1][1]
            bot[0][1] %= my
        map = [["." for c in range(mx)] for l in range(my)]
        for (x, y), (_, __) in bots:
            map[y][x] = "O"
        map2 = ["".join(l) for l in map]
        for i in range(my):
            if "OOOOOOO" in map2[i]:
                return t
