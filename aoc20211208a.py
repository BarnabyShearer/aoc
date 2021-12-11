def parse(d):
    return (
        ([frozenset(c) for c in g.split()] for g in l.split("|")) for l in d.split("\n")
    )


def aoc(data):
    return sum(len(d) in (2, 3, 4, 7) for _, b in parse(data) for d in b)
