def aoc(data):
    w = data.index("\n") + 1
    bugs = tuple([c == "#" for c in data])
    moves = [-w, -1, 1, w]
    seen = set()
    while True:
        if bugs in seen:
            break
        seen.add(bugs)
        newbugs = []
        for i, b in enumerate(bugs):
            s = sum([0 <= i + m < len(bugs) and bugs[i + m] for m in moves])
            newbugs.append(((i + 1) % w > 0) and ((s == 1) or (not b and (s == 2))))
        bugs = tuple(newbugs)
    total = 0
    v = 0
    for i, c in enumerate(bugs):
        if (i + 1) % w == 0:
            continue
        if c:
            total += 2**v
        v += 1
    return total
