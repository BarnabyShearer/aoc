from aoc20241219a import match


def aoc(data):
    t, d = data.split("\n\n")
    t = t.split(", ")
    d = d.split("\n")
    total = 0
    for dd in d:
        total += match(t, dd)
    return total
