from math import inf


def parse(data):
    return [
        (
            (int(b.split()[6]), 0, 0, 0),
            (int(b.split()[12]), 0, 0, 0),
            (int(b.split()[18]), int(b.split()[21]), 0, 0),
            (int(b.split()[27]), 0, int(b.split()[30]), 0),
        )
        for b in data.split("\n")
    ]


def score(blueprint, bots, materials, time):
    newbots, materials = [0, 0, 0, 0], list(materials)
    for _ in range(time):
        for i, bot in enumerate(bots):
            materials[i] += bot + newbots[i]
        for i, bp in enumerate(blueprint):
            if all(
                materials[ii] >= cost * (newbots[i] + 1) for ii, cost in enumerate(bp)
            ):
                newbots[i] += 1
    return materials[-1]


def brute(blueprint, time):
    need = tuple(max(bp[material] for bp in blueprint) for material in range(3)) + (
        inf,
    )
    best, open = 0, [((1, 0, 0, 0), (0, 0, 0, 0), time)]
    while open:
        bots, materials, time = open.pop()
        if score(blueprint, bots, materials, time) < best:
            continue
        best = max(best, materials[-1] + bots[-1] * time)
        for i, bp in enumerate(blueprint):
            if bots[i] >= need[i]:
                continue
            delta = max(
                0
                if (demand := bp[ii] - materials[ii]) <= 0
                else inf
                if bot <= 0
                else (demand + bot - 1) // bot
                for ii, bot in enumerate(bots)
            )
            if delta < time:
                open.append(
                    (
                        tuple(
                            bot + (1 if ii == i else 0) for ii, bot in enumerate(bots)
                        ),
                        tuple(
                            mat + bot * (delta + 1) - cost
                            for mat, bot, cost in zip(materials, bots, bp)
                        ),
                        time - delta - 1,
                    )
                )
    return best


def aoc(data):
    return sum(i * brute(blueprint, 24) for i, blueprint in enumerate(parse(data), 1))
