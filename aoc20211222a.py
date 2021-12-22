def parse(data):
    for state, cube in (l.split() for l in data.split("\n")):
        yield state == "on", tuple(
            tuple(int(c) for c in cord[2:].split("..")) for cord in cube.split(",")
        )


def subd(a, b):
    if a[0] == b[0]:
        if a[1] < b[1]:
            yield a
            yield (a[1] + 1, b[1])
        elif a[1] > b[1]:
            yield b
            yield (b[1] + 1, a[1])
        else:
            yield a
    elif a[0] < b[0] <= a[1]:
        yield (a[0], b[0] - 1)
        if a[1] == b[1]:
            yield b
        elif a[1] < b[1]:
            yield (b[0], a[1])
            yield (a[1] + 1, b[1])
        else:
            yield b
            yield (b[1] + 1, a[1])
    elif b[0] < a[0] <= b[1]:
        yield (b[0], a[0] - 1)
        if a[1] == b[1]:
            yield a
        elif a[1] < b[1]:
            yield a
            yield (a[1] + 1, b[1])
        else:
            yield (a[0], b[1])
            yield (b[1] + 1, a[1])
    else:
        yield a
        yield b


def incube(c, cube):
    return (
        cube[0][0] <= c[0][0] <= cube[0][1]
        and cube[1][0] <= c[1][0] <= cube[1][1]
        and cube[2][0] <= c[2][0] <= cube[2][1]
    )


def sub(a, b):
    for x in subd(a[0], b[0]):
        for y in subd(a[1], b[1]):
            for z in subd(a[2], b[2]):
                if not incube((x, y, z), b) and incube((x, y, z), a):
                    yield (x, y, z)


def dedup(cubes):
    seen = {}
    for x, y, z in cubes:
        if (x, y) in seen:
            if seen[(x, y)][1] == z[0] - 1:
                seen[(x, y)] = (seen[(x, y)][0], z[1])
            else:
                yield (x, y, z)
        else:
            seen[(x, y)] = z
    seen2 = {}
    for (x, y), z in seen.items():
        if (x, z) in seen2:
            if seen2[(x, z)][1] == y[0] - 1:
                seen2[(x, z)] = (seen2[(x, z)][0], y[1])
            else:
                yield (x, y, z)
        else:
            seen2[(x, z)] = y
    seen3 = {}
    for (x, z), y in seen2.items():
        if (y, z) in seen3:
            if seen3[(y, z)][1] == x[0] - 1:
                seen3[(y, z)] = (seen3[(y, z)][0], x[1])
            else:
                yield (x, y, z)
        else:
            seen3[(y, z)] = x
    for (y, z), x in seen3.items():
        yield (x, y, z)


def deoverlap(data):
    _, first = next(data)
    cubes = set((first,))
    for i, (state, newcube) in enumerate(data):
        newcubes = set()
        for cube in cubes:
            newcubes.update(dedup(sub(cube, newcube)))
        if state:
            newcubes.add(newcube)
        cubes = newcubes
    return cubes


def area(cubes):
    total = 0
    for cube in cubes:
        total += (
            (abs(cube[0][1] - cube[0][0]) + 1)
            * (abs(cube[1][1] - cube[1][0]) + 1)
            * (abs(cube[2][1] - cube[2][0]) + 1)
        )
    return total


def aoc(data):
    return area(deoverlap(c for c in parse(data) if -50 <= c[1][0][0] <= 50))
