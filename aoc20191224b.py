def aoc(data):
    space = {}
    for y in range(5):
        for x in range(5):
            nab = []
            if x == 0:
                nab.append((-1, 1, 2))
                nab.append((0, 1, y))
            elif x == 1:
                nab.append((0, 0, y))
                if y == 2:
                    for i in range(5):
                        nab.append((1, 0, i))
                else:
                    nab.append((0, 2, y))
            elif x == 2:
                if y != 2:
                    nab.append((0, 1, y))
                    nab.append((0, 3, y))
            elif x == 3:
                if y == 2:
                    for i in range(5):
                        nab.append((1, 4, i))
                else:
                    nab.append((0, 2, y))
                nab.append((0, 4, y))
            elif x == 4:
                nab.append((0, 3, y))
                nab.append((-1, 3, 2))
            if y == 0:
                nab.append((-1, 2, 1))
                nab.append((0, x, 1))
            elif y == 1:
                nab.append((0, x, 0))
                if x == 2:
                    for i in range(5):
                        nab.append((1, i, 0))
                else:
                    nab.append((0, x, 2))
            elif y == 2:
                if x != 2:
                    nab.append((0, x, 1))
                    nab.append((0, x, 3))
            elif y == 3:
                if x == 2:
                    for i in range(5):
                        nab.append((1, i, 4))
                else:
                    nab.append((0, x, 2))
                nab.append((0, x, 4))
            elif y == 4:
                nab.append((0, x, 3))
                nab.append((-1, 2, 3))
            space[(x, y)] = tuple(nab)
    for y in range(5):
        for x in range(5):
            print(x, y, space[(x, y)])

    bugs = {}
    for y, line in enumerate(data.split()):
        for x, c in enumerate(line):
            if c == "#":
                bugs[(0, x, y)] = True

    for i in range(200):
        newbugs = {}
        for z in range(-200, 200):
            for y in range(5):
                for x in range(5):
                    s = sum([(z + dz, dx, dy) in bugs for dz, dx, dy in space[(x, y)]])
                    if s == 1 or not (z, x, y) in bugs and s == 2:
                        newbugs[(z, x, y)] = True
        bugs = newbugs
    return len(bugs)
