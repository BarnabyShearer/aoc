def parse(line):
    return [int(n) for n in line.split("x")]


def wrap(w, l, h):
    size = [l * w, w * h, h * l]
    return sum(size) * 2 + min(size)


def aoc(data):
    return sum([wrap(*parse(line)) for line in data.split("\n")])
