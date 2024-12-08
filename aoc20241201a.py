def parse(data):
    a, b = [], []
    for l in data.split("\n"):
        aa, bb = (int(i) for i in l.split())
        a.append(aa)
        b.append(bb)
    return a, b


def aoc(data):
    a, b = parse(data)
    return sum(abs(aa - bb) for aa, bb in zip(sorted(a), sorted(b)))
