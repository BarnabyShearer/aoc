def cpu(data, x=1):
    for v in data.split():
        yield x
        if not v == "noop" and not v == "addx":
            x += int(v)


def aoc(data, mesure={20, 60, 100, 140, 180, 220}):
    return sum(x * i for i, x in enumerate(cpu(data), 1) if i in mesure)
