N = (
    (
        (-1, -1),
        (0, -1),
        (1, -1),
    ),
    (0, -1),
)
S = (
    (
        (-1, 1),
        (0, 1),
        (1, 1),
    ),
    (0, 1),
)
W = (
    (
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ),
    (-1, 0),
)
E = (
    (
        (1, -1),
        (1, 0),
        (1, 1),
    ),
    (1, 0),
)

CORDS = N[0] + S[0] + E[0] + W[0]


def parse(data):
    elves = set()
    for y, line in enumerate(data.split("\n")):
        for x, c in enumerate(line):
            if c == "#":
                elves.add((x, y))
    return elves


def step(elves, check):
    prop = set()
    bump = set()
    for x, y in elves:
        if any((x + xx, y + yy) in elves for xx, yy in CORDS):
            for cord, (mx, my) in check:
                if not any((x + xx, y + yy) in elves for xx, yy in cord):
                    if (x + mx, y + my) in prop:
                        bump.add((x + mx, y + my))
                    prop.add((x + mx, y + my))
                    break

    next = set()
    for x, y in elves:
        if any((x + xx, y + yy) in elves for xx, yy in CORDS):
            for cord, (mx, my) in check:
                if not any((x + xx, y + yy) in elves for xx, yy in cord):
                    if (x + mx, y + my) not in bump:
                        x += mx
                        y += my
                    break
        next.add((x, y))
    elves = next
    check = check[1:] + [check[0]]
    return elves, check


def aoc(data):
    elves = parse(data)
    check = [N, S, W, E]
    for _ in range(10):
        elves, check = step(elves, check)

    area = (1 + max(*(x for x, _ in elves)) - min(*(x for x, _ in elves))) * (
        1 + max(*(y for _, y in elves)) - min(*(y for _, y in elves))
    )

    return area - len(elves)
