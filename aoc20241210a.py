from aoc20241204a import g


def find(seen, data, x, y, i):
    if g(g(data, y), x) != i:
        return 0
    if i == 9:
        if seen == False or (x, y) not in seen:
            if seen != False:
                seen.add((x, y))
            return 1
        return 0
    return sum(
        find(seen, data, x + dx, y + dy, i + 1)
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))
    )


def parse(data):
    return [[int(i) if i != "." else "." for i in l] for l in data.split("\n")]


def aoc(data):
    data = parse(data)
    return sum(
        sum(find(set(), data, x, y, 0) for x in range(len(l)))
        for y, l in enumerate(data)
    )
