from aoc20241210a import parse, find


def aoc(data):
    data = parse(data)
    return sum(
        sum(find(False, data, x, y, 0) for x in range(len(l)))
        for y, l in enumerate(data)
    )
