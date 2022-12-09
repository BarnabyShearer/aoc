def parse(data):
    return [[int(x) for x in y] for y in data.split("\n")]


def maxe(d):
    return max((-1, *d))


def aoc(data):
    total = 0
    data = parse(data)
    for y in range(len(data)):
        for x in range(len(data[y])):
            if maxe(data[y][:x]) < data[y][x] or maxe(data[y][x + 1 :]) < data[y][x]:
                total += 1
            else:
                if (
                    maxe(r[x] for r in data[:y]) < data[y][x]
                    or maxe(r[x] for r in data[y + 1 :]) < data[y][x]
                ):
                    total += 1
    return total
