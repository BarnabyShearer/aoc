def hash(v):
    hash = 0
    for c in v:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash


def aoc(data):
    return sum(hash(l) for l in data.split(","))
