def parse(data):
    kernel, img = data.split("\n\n")
    i = set()
    for y, r in enumerate(img.split()):
        for x, c in enumerate(r):
            if c == "#":
                i.add((x, y))
    return [c == "#" for c in kernel], i


def enhance(kernel, i, inverted):
    inverting = kernel[0] and not inverted
    e = set()
    for x, y in i:
        for ax, ay in ((x + dx, y + dy) for dy in range(-1, 2) for dx in range(-1, 2)):
            m = 0
            for dx, dy in (
                (ax + dx, ay + dy) for dy in range(-1, 2) for dx in range(-1, 2)
            ):
                m <<= 1
                m |= ((dx, dy) in i) != inverted
            if kernel[m] != inverting:
                e.add((ax, ay))
    return e, inverting


def aoc(data):
    kernel, i = parse(data)
    inverted = False
    for _ in range(2):
        i, inverted = enhance(kernel, i, inverted)
    return len(i)
