import random
import sys
from cpu import cpu

NAV = {1: (0, -1), 3: (1, 0), 2: (0, 1), 4: (-1, 0)}
PALLET = "█ x."


def move(x, y):
    return [(x + xx, y + yy, i) for i, (xx, yy) in NAV.items()]


def pathfind(seen, start, target):
    path = {target: 0}
    i = 0
    while start not in path:
        for x, y, _ in move(*list(path.keys())[i]):
            if seen.get((x, y), 0) != 0:
                path[(x, y)] = min(path.get((x, y), i + 1), i + 1)
        i += 1
    return path


def draw(seen, x, y):
    screen = "\033[2J"
    for yy in range(
        min([y for (x, y) in seen.keys()]), max([x for (x, y) in seen.keys()]) + 1
    ):
        for xx in range(
            min([x for (x, y) in seen.keys()]), max([x for (x, y) in seen.keys()]) + 1
        ):
            if yy == y and xx == x:
                screen += "@"
            else:
                screen += PALLET[seen.get((xx, yy), -1)]
        screen += "\n"
    screen += "\nx=" + str(x) + ", y=" + str(y) + "\n"
    sys.stdout.write(screen)
    sys.stdout.flush()


def discover_map(data):
    c = cpu(data)
    seen = {(0, 0): 1}
    x, y = (0, 0)
    search = set()
    count = 0
    target = None
    while True:
        next(c)
        count += 1
        search |= set([(x, y) for x, y, _ in move(x, y)])
        search = {item for item in search if item not in seen}
        if not search:
            draw(seen, 0, 0)
            break
        if not target or target in seen:
            target = random.choice(tuple(search))
            path = pathfind(seen, (x, y), target)
        for xx, yy, d in move(x, y):
            if (xx, yy) not in seen and (x, y) in path:
                path[(xx, yy)] = path[(x, y)] + 1
                x, y = xx, yy
                break
            if (xx, yy) in path and path[(xx, yy)] <= path[(x, y)]:
                x, y = xx, yy
                break
        seen[(x, y)] = c.send(d)
        if seen[(x, y)] == 0:
            del path[(xx, yy)]
            x, y = x - NAV[d][0], y - NAV[d][1]
        if count % 1000 == 0:
            draw(seen, x, y)
    return seen


def aoc(data):
    return 0
    seen = discover_map(data)
    finish = [key for key, value in seen.items() if value == 2][0]
    path = pathfind(seen, (0, 0), finish)
    x, y = (0, 0)
    step = 0
    while (x, y) != finish:
        for xx, yy, d in move(x, y):
            if (xx, yy) in path and path[(xx, yy)] <= path[(x, y)]:
                x, y = xx, yy
                step += 1
                break
    return step
