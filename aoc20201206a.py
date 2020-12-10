def aoc(data):
    total = 0
    for group in data.split("\n\n"):
        unique = set()
        for q in group.replace("\n", ""):
            unique.add(q)
        total += len(unique)
    return total
