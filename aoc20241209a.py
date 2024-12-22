def aoc(data):
    data = [int(i) for i in data]
    files = list(enumerate(data[::2]))
    rle = []
    for b in data[1::2]:
        (i, a), *files = files
        rle.append((a, i))
        if not files:
            break
        ii, r = files.pop()
        while r < b:
            rle.append((r, ii))
            b -= r
            ii, r = files.pop()
        rle.append((b, ii))
        if r - b > 0:
            files.append((ii, r - b))
        if not files:
            break
    total = 0
    i = 0
    for a, b in rle:
        if a:
            for i in range(i, i + a):
                total += i * b
            i += 1
    return total
