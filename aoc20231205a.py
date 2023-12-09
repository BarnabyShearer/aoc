import bisect


def parse(data):
    data = data.split("\n\n")
    seeds = (int(s) for s in data[0].split(": ")[1].split())
    maps = []
    for m in data[1:]:
        map = {-1: 0, float("inf"): 0}
        for a, b, c in (l.split() for l in m.split("\n")[1:]):
            map[int(b)] = int(a) - int(b)
            if int(b) + int(c) not in map:
                map[int(b) + int(c)] = 0
        maps.append((sorted(map.keys()), tuple(map[k] for k in sorted(map.keys()))))
    return seeds, maps


def lookup(breaks, values, v):
    return v + values[bisect.bisect(breaks, v) - 1]


def aoc(data):
    seeds, maps = parse(data)
    for breaks, values in maps:
        seeds = tuple(lookup(breaks, values, s) for s in seeds)
    return min(*seeds)
