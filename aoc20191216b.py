def aoc(data):
    off = int(data[:7])
    x = [int(x) for x in data] * 10000
    for phase in range(100):
        for i in range(-2, -len(x[off:]) - 1, -1):
            x[i] = (x[i] + x[i + 1]) % 10
    return int("".join([str(a) for a in x[off : off + 8]]))
