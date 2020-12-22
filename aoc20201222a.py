def parse(data):
    return (tuple(int(c) for c in deck.split("\n")[1:]) for deck in data.split("\n\n"))


def score(a):
    return sum(c * (i + 1) for i, c in enumerate(reversed(a)))


def aoc(data):
    a, b = parse(data)
    while a and b:
        aa, a = a[0], a[1:]
        bb, b = b[0], b[1:]
        if aa > bb:
            a += (aa, bb)
        else:
            b += (bb, aa)
    return score(a or b)
