def has_count(line, count):
    return any([line.count(x) == count for x in line])


def aoc(data):
    data = data.split("\n")
    return sum([has_count(x, 2) for x in data]) * sum([has_count(x, 3) for x in data])
