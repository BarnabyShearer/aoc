CACHE = dict()


def parse(data):
    lines = tuple(l.split(" ") for l in data.split("\n"))
    groups = tuple(tuple(int(g) for g in groups.split(",")) for _, groups in lines)
    lines = tuple(line for line, _ in lines)
    return lines, groups


def split(t, group, pre, post):
    if not post:
        tg = tuple(len(g) for g in pre.split(".") if g)
        if tg == group:
            return t + 1
        else:
            return 0
    if post[0] == "?":
        t += split(0, group, pre + "#", post[1:])
        tg = tuple(len(g) for g in pre.split(".") if g)
        if len(tg) > len(group) or group[: len(tg)] != tg:
            return t
        key = (group[len(tg) :], post[1:])
        if key not in CACHE:
            CACHE[key] = split(0, group, pre + ".", post[1:])
        return t + CACHE[key]
    else:
        return split(t, group, pre + post[0], post[1:])


def check(line, group):
    return group == tuple(len(g) for g in line.split(".") if g)


def aoc(data):
    total = 0
    lines, groups = parse(data)

    for line, group in zip(lines, groups):
        total += split(0, group, "", line)
    return total
