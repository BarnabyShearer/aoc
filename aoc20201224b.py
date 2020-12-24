from aoc20201224a import MAP, tiles


def aoc(data):
    prev = tiles(data)
    minx, maxx = min([x for x, y in prev]), max([x for x, y in prev])
    minx = minx // 2 * 2 - 2
    maxx = maxx // 2 * 2 + 2
    miny, maxy = min([y for x, y in prev]), max([y for x, y in prev])
    for _ in range(100):
        newtiles = {}
        for y in range(miny - (i + 1) * 3, maxy + (i + 1) * 3 + 1, 3):
            for x in range(
                (-1 if y % 6 else 0) + minx - (i + 1) * 2, maxx + (i + 1) * 2 + 1, 2
            ):
                s = sum((x + dx, y + dy) in prev for dx, dy in MAP.values())
                if s == 2 or s == 1 and (x, y) in prev:
                    newtiles[(x, y)] = True
        prev = newtiles
    return len(newtiles)
