from aoc20241206a import solve


def aoc(data):
    data = [list(l) for l in data.split("\n")]
    total = 0
    for x, y in solve(data):
        data2 = [[v for v in l] for l in data]
        data2[y][x] = "#"
        if not solve(data2):
            total += 1
    return total
