from time import sleep


def parse(data):
    e = set()
    s = set()
    for y, r in enumerate(data.split("\n")):
        for x, c in enumerate(r):
            if c == ">":
                e.add((x, y))
            if c == "v":
                s.add((x, y))
    return x + 1, y + 1, e, s


def move(w, h, e, s):
    while True:
        ne = set()
        ns = set()
        for x, y in e:
            xx = (x + 1) % w
            ne.add((x if (xx, y) in e or (xx, y) in s else xx, y))
        for x, y in s:
            yy = (y + 1) % h
            ns.add((x, y if (x, yy) in ne or (x, yy) in s else yy))
        if e == ne and s == ns:
            break
        e = ne
        s = ns
        yield w, h, e, s


def aoc(data):
    return len(list(move(*parse(data)))) + 1
