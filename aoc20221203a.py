def parse(data):
    return [(r[: len(r) // 2], r[len(r) // 2 :]) for r in data.split("\n")]


def score(l):
    return ord(l) - (ord("A") - 27 if ord(l) < ord("a") else ord("a") - 1)


def aoc(data):
    return sum(score((set(a) & set(b)).pop()) for a, b in parse(data))
