from math import ceil


def parse(data):
    return [[c if c in "[,]" else int(c) for c in l] for l in data.split()]


def incf(s, v):
    ret = []
    for c in s:
        if isinstance(c, str):
            ret.append(c)
        else:
            ret.append(c + v)
            v = 0
    return ret


def reduce(a):
    while True:
        d = 0
        for i, c in enumerate(a):
            if c == "[":
                d += 1
                if d > 4:
                    a = (
                        incf(a[:i][::-1], a[i + 1])[::-1]
                        + [0]
                        + incf(a[i + 5 :], a[i + 3])
                    )
                    break
            elif c == "]":
                d -= 1
        else:
            for i, c in enumerate(a):
                if isinstance(c, int) and c > 9:
                    a = a[:i] + ["[", c // 2, ",", ceil(c / 2), "]"] + a[i + 1 :]
                    break
            else:
                return a


def add(a, b):
    return reduce(["["] + a + [","] + b + ["]"])


def magnitude(a):
    if isinstance(a, int):
        return a
    else:
        return 3 * magnitude(a[0]) + 2 * magnitude(a[1])


def i_am_lazy(a):
    return eval("".join(str(c) for c in a))


def aoc(data):
    data = parse(data)
    total = data[0]
    for num in data[1:]:
        total = add(total, num)
    return magnitude(i_am_lazy(total))
