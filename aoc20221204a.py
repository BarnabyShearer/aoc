def to_range(r):
    s, e = [int(a) for a in r.split("-")]
    return set(range(s, e + 1))


def parse(data):
    return ((to_range(a) for a in e) for e in (r.split(",") for r in data.split("\n")))


def aoc(data):
    return sum(1 for a, b in parse(data) if a.issubset(b) or b.issubset(a))
