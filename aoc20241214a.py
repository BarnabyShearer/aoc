def parse(data):
    for l in data.split("\n"):
        yield [[int(ii) for ii in i[2:].split(",")] for i in l.split(" ")]


def aoc(data):
    mx, my = 101, 103
    a, b, c, d = 0, 0, 0, 0

    for (px, py), (vx, vy) in parse(data):
        for i in range(100):
            px += vx
            px %= mx
            py += vy
            py %= my

        if px < mx // 2:
            if py < my // 2:
                a += 1
            elif py > my // 2:
                b += 1
        elif px > mx // 2:
            if py < my // 2:
                c += 1
            elif py > my // 2:
                d += 1
    return a * b * c * d
