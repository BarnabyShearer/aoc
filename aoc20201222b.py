from aoc20201222a import parse, score


def game(a, b):
    oa, ob = a, b
    seen = set()
    while a and b:
        if (a, b) in seen:
            return [0], []
        seen.add((a, b))
        aa, a = a[0], a[1:]
        bb, b = b[0], b[1:]
        if aa <= len(a) and bb <= len(b):
            if game(a[:aa], b[:bb])[0]:
                a += (aa, bb)
            else:
                b += (bb, aa)
        elif aa > bb:
            a += (aa, bb)
        else:
            b += (bb, aa)
    return a, b


def aoc(data):
    aa, bb = game(*parse(data))
    return score(aa or bb)
