def parse(data):
    return [
        [int(x) if x.replace("-", "").isdigit() else x for x in l.split()]
        for l in data.split("\n")
    ]


def calc(data):
    # ¯\_(ツ)_/¯ Just use the values that mater, automating decompile was too hard
    stack = []
    for i in range(len(data) // 18):
        if data[i * 18 + 5][2] > 0:
            stack.append((i, data[i * 18 + 15][2]))
        else:
            ii, offset = stack.pop()
            yield i, ii, offset + data[i * 18 + 5][2]


def aoc(data):
    digits = [9] * 14
    for i, ii, offset in calc(parse(data)):
        if offset > 0:
            digits[ii] -= offset
        else:
            digits[i] += offset
    return "".join(str(d) for d in digits)
