def aoc(data):
    total = 0
    min, max = data.split("-")
    for x in [str(x) for x in range(int(min), int(max))]:
        inc = True
        double = False
        for i, d in enumerate(x[1:]):
            if d < x[i]:
                inc = False
                break

        for i, d in enumerate(x):
            if d != (" " + x)[i] and d == (x + " ")[i + 1] and d != (x + "  ")[i + 2]:
                double = True
        if double and inc:
            total += 1
    return total
