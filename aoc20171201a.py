def same(data, offset=1):
    for i, d in enumerate(data):
        if d == data[(i + offset) % len(data)]:
            yield d


def aoc(data):
    return sum(same([int(d) for d in data]))
