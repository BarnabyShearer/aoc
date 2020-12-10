def parse(data):
    result = {}
    for c, o in [line.split(")") for line in data.split("\n")]:
        if c not in result:
            result[c] = set()
        if o not in result:
            result[o] = set()
        result[c].add(o)
        result[o].add(c)
    return result


def dijkstra(orbits, src, dest):
    q = set(orbits.keys())
    dist = {}
    prev = {}
    for o in q:
        dist[o] = 0 if src == o else 999999
        prev[o] = None
    while q:
        u = min(q, key=dist.get)
        if u == dest:
            break
        q.remove(u)
        for v in orbits.get(u, []):
            if v in q:
                alt = dist[u] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u
    route = [dest]
    while route[0]:
        route.insert(0, prev[route[0]])
    print(route[1:])
    return route[1:]


def aoc(data):
    return len(dijkstra(parse(data), "YOU", "SAN")) - 3
