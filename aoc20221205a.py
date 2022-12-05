from collections import defaultdict


def parse_creates(data):
    creates = defaultdict(lambda: [])
    for r in data.split("\n")[-1::-1]:
        for s, c in enumerate(r[1::4]):
            if c != " ":
                creates[s + 1].append(c)
    return creates


def parse_op(data):
    return (
        (int(c), int(a), int(b))
        for _move, c, _from, a, _to, b in (r.split() for r in data.split("\n"))
    )


def parse(data):
    c, o = data.split("\n\n")
    return parse_creates(c), parse_op(o)


def output(creates):
    return "".join(creates[i].pop() for i in range(1, 10))


def aoc(data):
    creates, ins = parse(data)
    for c, a, b in ins:
        for _ in range(c):
            creates[b].append(creates[a].pop())
    return output(creates)
