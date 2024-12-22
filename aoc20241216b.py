from aoc20241216a import solve


def aoc(data):
    data = data.split("\n")
    seen, best, end = solve(data)
    seat = set()
    open = set(
        [
            (*end, 0, -1, best + 1, (end,)),
            (*end, 0, 1, best + 1, (end,)),
            (*end, 1, 0, best + 1, (end,)),
            (*end, -1, 0, best + 1, (end,)),
        ]
    )
    while open:
        newopen = set()
        for x, y, dx, dy, best, path in open:
            if data[y][x] == "S":
                seat |= set(path)
            if seen[(x, y, dx, dy)] < best:
                path = (*path, (x, y))
                newopen.add((x - dx, y - dy, dx, dy, seen[(x, y, dx, dy)], path))
                newopen.add((x, y, -dy, dx, seen[(x, y, dx, dy)], path))
                newopen.add((x, y, dy, -dx, seen[(x, y, dx, dy)], path))
        open = newopen

    return len(seat)
