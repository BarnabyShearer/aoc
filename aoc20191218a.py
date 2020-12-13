def findkeys(data, map, pos, have):
    path = [(pos, 0)]
    seen = set()
    while path:
        pos, cost = path.pop(0)
        if data[pos].islower() and data[pos] not in have:
            yield cost, pos, data[pos]
            continue
        for p in [pos + p for p in map]:
            if p in seen:
                continue
            seen.add(p)
            if data[p] != "#" and (not data[p].isupper() or data[p].lower() in have):
                path.append((p, cost + 1))


def search(data):
    keys = set(data.lower()) - set("#@.\n")
    w = data.index("\n") + 1
    map = [-w, -1, 1, w]
    seen = set()
    q = [
        (0, tuple(i for i, v in enumerate(data) if v == "@"), frozenset()),
    ]
    while True:
        steps, positions, have = q.pop(0)
        if have == keys:
            return steps
        if (positions, have) in seen:
            continue
        seen.add((positions, have))
        for i, pos in enumerate(positions):
            for cost, pos, key in findkeys(data, map, pos, have):
                q = sorted(
                    q
                    + [
                        (
                            steps + cost,
                            positions[:i] + (data.index(key),) + positions[i + 1 :],
                            have | set((key,)),
                        )
                    ]
                )


def aoc(data):
    return search(data)
