from itertools import cycle


def parse(data):
    dir, data = data.split("\n\n")
    nodes = {
        l.split(" =")[0]: (l.split(" = (")[1].split(", ")[0], l.split(", ")[1][:-1])
        for l in data.split("\n")
    }
    return len(dir), cycle({"R": 1, "L": 0}[d] for d in dir), nodes


def aoc(data):
    node = "AAA"
    _, dir, nodes = parse(data)
    for s, d in enumerate(dir):
        if node == "ZZZ":
            break
        node = nodes[node][d]
    return s
