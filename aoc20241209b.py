def aoc(data):
    data = "2333133121414131402"
    data = [int(i) for i in data]
    files = []
    spaces = []
    i = 0
    ii = 0
    for f, (a, b) in enumerate(zip(data[::2], data[1::2] + [0])):
        files.append((i, a, ii))
        i += a
        spaces.append((i, b))
        i += b
        ii += 1
    total = 0
    for fi, f, ii in reversed(files):
        for iii, (si, s) in enumerate(spaces):
            if s >= f:
                if fi > si:
                    spaces[iii] = (si + f, s - f)
                    for iiii in range(si, si + f):
                        total += iiii * ii
                    break
        else:
            for iiii in range(fi, fi + f):
                total += iiii * ii
    return total
