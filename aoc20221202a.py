SCORE = {0: 3, 1: 0, 2: 6}


def parse(data):
    return [
        (ord(a) - ord("A"), ord(b) - ord("X"))
        for a, b in [r.split() for r in data.split("\n")]
    ]


def aoc(data):
    return sum(1 + me + SCORE[(them - me) % 3] for them, me in parse(data))
