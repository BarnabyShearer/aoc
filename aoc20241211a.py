SEEN = {}


def do(s, depth):
    if (s, depth) in SEEN:
        return SEEN[(s, depth)]
    if depth == 0:
        r = 1
    elif s == 0:
        r = do(1, depth - 1)
    elif len(str(s)) % 2 == 0:
        r = do(int(str(s)[: len(str(s)) // 2]), depth - 1) + do(
            int(str(s)[len(str(s)) // 2 :]), depth - 1
        )
    else:
        r = do(s * 2024, depth - 1)
    SEEN[(s, depth)] = r
    return r


def aoc(data):
    total = 0
    for c in [int(i) for i in data.split()]:
        total += do(c, 25)
    return total
