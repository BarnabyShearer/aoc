from aoc20211212a import *


def aoc(data):
    data = parse(data)
    scenic = set()
    for a in data.keys() - ("start", "end"):
        if a == a.lower():
            scenic.update(routes(data, ("start",), a))
    return len(scenic)
