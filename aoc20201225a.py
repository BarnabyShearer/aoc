def aoc(data):
    a, b = (int(x) for x in data.split())
    n = 1
    i = 0
    while n != a:
        n *= 7
        n %= 20201227
        i += 1
    n = 1
    for _ in range(i):
        n *= b
        n %= 20201227
    return n
