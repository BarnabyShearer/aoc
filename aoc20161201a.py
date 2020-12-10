MAP = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def steps(data):
    x, y, face = (0, 0, 0)
    for dir, len in [(x[0], int(x[1:])) for x in data.split(", ")]:
        face += 1 if dir == "R" else -1
        face %= 4
        for _ in range(len):
            x += MAP[face][0]
            y += MAP[face][1]
            yield x, y


def aoc(data):
    *_, (x, y) = steps(data)
    return abs(x) + abs(y)
