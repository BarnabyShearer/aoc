from aoc20241202a import ok


def aoc(data):
    total = 0
    for r in data.split("\n"):
        for s in range(len(r.split())):
            if ok(int(i) for ii, i in enumerate(r.split()) if ii != s):
                total += 1
                break
    return total
