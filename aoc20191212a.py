def parse(data):
    return [
        [int(cord.split("=")[-1]) for cord in moon[1:-1].split(",")]
        for moon in data.split("\n")
    ]


def step(moon, d):
    for a in moon:
        for b in moon:
            if b[d] > a[d]:
                a[d + 3] += 1
            if b[d] < a[d]:
                a[d + 3] -= 1
    for a in moon:
        a[d] += a[d + 3]


def aoc(data):
    moon = [m + [0, 0, 0] for m in parse(data)]
    for _ in range(1000):
        for d in range(3):
            step(moon, d)
    total = 0
    for a in moon:
        mag = [abs(x) for x in a]
        total += sum(mag[:3]) * sum(mag[3:])
    return total
