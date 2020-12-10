from aoc20151203a import visited


def aoc(data):
    return len(visited(data[::2]) | visited(data[1::2]))
