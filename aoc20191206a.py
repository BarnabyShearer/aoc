def parse(data):
    result = {}
    for c, o in [line.split(")") for line in data.split("\n")]:
        if c not in result:
            result[c] = set()
        result[c].add(o)
    return result


def aoc(data):
    orbits = parse(data)
    total = 0
    visited = set()
    to = set((("COM", 0),))
    while to:
        current, dist = to.pop()
        for o in orbits.get(current, []):
            if o not in visited:
                to.add((o, dist + 1))
        visited.add(current)
        total += dist
    return total
