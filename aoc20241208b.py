from aoc20241208a import parse, clean, calc


def aoc(data):
    t, w, h = parse(data)
    return len(clean(calc(t, range(50)), w, h))
