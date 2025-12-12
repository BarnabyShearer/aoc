from itertools import pairwise


def tomap(data):
    return {c: (x, y) for y, l in enumerate(data.split("\n")) for x, c in enumerate(l)}


D = tomap("""789
456
123
 0A""")

R = tomap(""" ^A
<v>""")


def step(D, d, c):
    h, v = "", ""
    if D[d][0] < D[c][0]:
        h += ">" * (D[c][0] - D[d][0])
    if D[d][0] > D[c][0]:
        h += "<" * (D[d][0] - D[c][0])
    if D[d][1] > D[c][1]:
        v += "^" * (D[d][1] - D[c][1])
    if D[d][1] < D[c][1]:
        v += "v" * (D[c][1] - D[d][1])
    if D[d][1] != D[" "][1] or D[c][0] != D[" "][0]:
        yield h + v + "A"
    if D[d][0] != D[" "][0] or D[c][1] != D[" "][1]:
        yield v + h + "A"


def do(CACHE, code, robots):
    total = 0
    for pad_old, pad_next in pairwise("A" + code):
        scores = []
        for pad in step(D, pad_old, pad_next):
            score = 0
            for pad_d, pad_c in pairwise("A" + pad):
                if (pad_d, pad_c) not in CACHE:
                    inputs = (pad_d + pad_c,)
                    for _ in range(robots):
                        print(_)
                        outputs = set()
                        for input in inputs:
                            buttons = set(("A",))
                            for d, c in pairwise(input):
                                oldbuttons = buttons
                                buttons = set()
                                for a in step(R, d, c):
                                    for b in oldbuttons:
                                        buttons.add(b + a)
                            outputs |= buttons
                        inputs = outputs
                    CACHE[(pad_d, pad_c)] = min(len(b) for b in inputs) - 1
                score += CACHE[(pad_d, pad_c)]
            scores.append(score)
        total += min(scores)
    print(total, int(code[:-1]))
    return total * int(code[:-1])


def aoc(data):
    total = 0
    for l in data.split("\n"):
        total += do({}, l, 2)
    return total
