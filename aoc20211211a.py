CASCADE = tuple((x, y) for x in range(-1, 2) for y in range(-1, 2))


def parse(data):
    return [[int(c) for c in r] for r in data.split("\n")]


def step(data, flash):
    data = [[c + 1 for c in r] for r in data]

    oldflash = -1
    while flash != oldflash:
        oldflash = flash
        for y, r in enumerate(data):
            for x, c in enumerate(r):
                if c == 10:
                    flash += 1
                    for dx, dy in ((x + dx, y + dy) for dx, dy in CASCADE):
                        if 0 <= dx <= 9 and 0 <= dy <= 9 and data[dy][dx] != 10:
                            data[dy][dx] += 1
                    data[y][x] += 1

    data = [[0 if c > 9 else c for c in r] for r in data]
    return data, flash


def aoc(data):
    total = 0
    data = parse(data)
    for _ in range(100):
        data, total = step(data, total)
    return total
