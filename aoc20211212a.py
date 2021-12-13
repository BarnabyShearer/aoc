from collections import defaultdict


def parse(data):
    conn = defaultdict(lambda: set())
    for a, b in (r.split("-") for r in data.split("\n")):
        conn[a].add(b)
        conn[b].add(a)
    return conn


def routes(data, route, double=""):
    if route[-1] == "end":
        yield route
    for b in data[route[-1]]:
        if b == b.upper() or b not in route or (b == double and route.count(b) == 1):
            yield from routes(data, route + (b,), double)


def aoc(data):
    return len(list(routes(parse(data), ("start",))))
