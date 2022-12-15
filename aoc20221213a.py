from math import inf


def parse(data):
    for p in data.split("\n\n"):
        yield (eval(l) for l in p.split())


def comp(a, b):
    if isinstance(a, list):
        if isinstance(b, list):
            for aa, bb in zip(a, b):
                if (ret := comp(aa, bb)) != 0:
                    return ret
            if len(a) < len(b):
                return -1
            if len(b) < len(a):
                return 1
        else:
            return comp(a, [b])
    else:
        if isinstance(b, list):
            return comp([a], b)
        else:
            if a < b:
                return -1
            if b < a:
                return 1
    return 0


def aoc(data):
    return sum(i for i, (a, b) in enumerate(parse(data), 1) if comp(a, b) == -1)
