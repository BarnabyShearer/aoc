def surround(map, data, pos):
    return len([True for p in map if 0 <= pos + p < len(data) and data[pos + p] == "#"])


def step(map, data):
    for pos, seat in enumerate(data):
        if seat == "#":
            yield "L" if surround(map, data, pos) >= 4 else "#"
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
