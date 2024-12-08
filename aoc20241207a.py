def solve(data, f):
    total = 0
    for t, v in (l.split(": ") for l in data.split("\n")):
        prev = set((0,))
        n = set()
        for vv in v.split():
            for p in prev:
                for r in f(p, int(vv)):
                    n.add(r)
            prev = n
            n = set()
        if int(t) in prev:
            total += int(t)
    return total


def aoc(data):
    return solve(data, lambda a, b: (a + b, a * b))
