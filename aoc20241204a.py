def g(l, n):
    if n < 0:
        return []
    try:
        return l[n]
    except IndexError:
        return []


def aoc(data):
    total = 0
    data = data.split("\n")
    for y, yy in enumerate(data):
        for x, xx in enumerate(yy):
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if all(
                        g(g(data, y + dy * i), x + dx * i) == c
                        for i, c in enumerate("XMAS")
                    ):
                        dd = [
                            ["." for __ in range(len(data[0]))]
                            for _ in range(len(data))
                        ]
                        for ii, cc in enumerate("XMAS"):
                            dd[y + dy * ii][x + dx * ii] = cc
                        total += 1
    return total
