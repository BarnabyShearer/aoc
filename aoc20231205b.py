from aoc20231205a import *


def grouper(n, iterable):
    args = [iter(iterable)] * n
    return zip(*args)


def aoc(data):

    seeds, maps = parse(data)
    seeds = tuple((a, a + b - 1) for a, b in grouper(2, seeds))
    for breaks, values in maps:
        nextseeds = []
        for a, b in seeds:
            end = breaks[bisect.bisect(breaks, a)]
            while end < b:
                nextseeds.append(
                    (lookup(breaks, values, a), lookup(breaks, values, end - 1))
                )
                a = end
                end = breaks[bisect.bisect(breaks, end)]
            if end >= b:
                nextseeds.append((lookup(breaks, values, a), lookup(breaks, values, b)))
        seeds = nextseeds

    return min(*(a for a, _ in seeds))
