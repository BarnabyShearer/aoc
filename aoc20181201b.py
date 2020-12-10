def aoc(data):
    total = 0
    seen = set()
    while True:
        for delta in [int(x) for x in data.split("\n")]:
            total += delta
            if total in seen:
                return total
            seen.add(total)
