def aoc(data):
    total = 0
    min, max = data.split("-")
    for x in range(int(min), int(max)):
        double = False
        inc = True
        prev = "0"
        for d in str(x):
            if d < prev:
                inc = False
                break
            if d == prev:
                double = True
            prev = d
        if double and inc:
            total += 1
    return total
