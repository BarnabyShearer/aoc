def surround(map, data, pos):
    total = 0
    for dir in map:
        p = pos + dir
        while 0 <= p < len(data):
            if data[p] == "#":
                total += 1
                break
            elif data[p] == "L":
                break
            elif data[p] == "\n":
                break
            p += dir
    return total


def step(map, data):
    for pos, seat in enumerate(data):
        if seat == "#":
            yield "L" if surround(map, data, pos) >= 5 else "#"
        elif seat == "L":
            yield "#" if surround(map, data, pos) == 0 else "L"
        else:
            yield seat


def aoc(data):
    w = data.index("\n") + 1
    map = [-w - 1, -w, -w + 1, -1, +1, +w - 1, +w, +w + 1]
    prev = ""
    while data != prev:
        prev = data
        data = "".join(step(map, data))
    return data.count("#")
