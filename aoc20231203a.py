def get_parts(data):
    data = [f".{l}." for l in data.split("\n")]
    data = ["." * len(data), *data, "." * len(data)]
    s, sx, sy, n, parts = None, None, None, 0, []
    for y, l in enumerate(data):
        for x, c in enumerate(l):
            if c.isnumeric():
                n *= 10
                n += int(c)
                for xx, yy in ((x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]):
                    t = data[y + yy][x + xx]
                    if t != "." and not t.isnumeric():
                        s = t
                        sx = x + xx
                        sy = y + yy
            else:
                if s:
                    parts.append((s, sx, sy, n))
                n = 0
                s = None
    return parts


def aoc(data):
    return sum(p[-1] for p in get_parts(data))
