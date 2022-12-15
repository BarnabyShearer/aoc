from aoc20211201a import window


def parse(data):
    return [
        [[int(o) for o in c.split(",")] for c in l.split(" -> ")]
        for l in data.split("\n")
    ]


def rock(lines):
    depth = 0
    w = set()
    for l in lines:
        for (x1, y1), (x2, y2) in window(l):
            depth = max(depth, y1, y2)
            if y1 == y2:
                for xx in range(min(x1, x2), max(x1, x2) + 1):
                    w.add((xx, y1))
            else:
                for yy in range(min(y1, y2), max(y1, y2) + 1):
                    w.add((x1, yy))
    return w, depth


def sand(w, depth, closed=False):
    for i in range(9999999):
        sx, sy = 500, 0
        for sy in range(depth):
            if closed and sy + 1 == depth:
                w.add((sx, sy))
                break
            if not (sx, sy + 1) in w:
                continue
            if not (sx - 1, sy + 1) in w:
                sx -= 1
                continue
            if not (sx + 1, sy + 1) in w:
                sx += 1
                continue
            w.add((sx, sy))
            if sy == 0:
                return i + 1
            break
        else:
            return i


def aoc(data):
    return sand(*rock(parse(data)))
