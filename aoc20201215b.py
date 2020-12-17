def aoc(data):
    seen = {}
    said = [int(n) for n in data.split(",")]
    last = None
    for i, n in enumerate(said):
        if last is not None:
            seen[last] = i
        last = n
    for i in range(len(said), 30000000):
        prev = last
        if last in seen:
            last = i - seen[last]
        else:
            last = 0
        seen[prev] = i
    return last
