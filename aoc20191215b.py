from aoc20191215a import discover_map, move, draw


def aoc(data):
    seen = discover_map(data)
    step = 0
    while 1 in seen.values():
        prev = seen.copy()
        for (x, y), value in prev.items():
            if value == 2:
                for xx, yy, _ in move(x, y):
                    if prev[(xx, yy)] == 1:
                        seen[(xx, yy)] = 2
        draw(seen, 0, 0)
        step += 1
    return step
