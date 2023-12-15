from itertools import combinations


def gaps(data):
    for i, l in enumerate(data):
        if all(c == "." for c in l):
            yield i


def star(data):
    for y, l in enumerate(data):
        for x, c in enumerate(l):
            if c == "#":
                yield (x, y)


def aoc(data, enlarge=1):
    total = 0
    data = data.split("\n")
    gaps_x, gaps_y = set(gaps(zip(*data))), set(gaps(data))
    for (x, y), (xx, yy) in combinations(star(data), 2):
        total += abs(xx - x) + abs(yy - y)
        for xxx in range(min(x, xx), max(x, xx)):
            if xxx in gaps_x:
                total += enlarge
        for yyy in range(min(y, yy), max(y, yy)):
            if yyy in gaps_y:
                total += enlarge
    return total
