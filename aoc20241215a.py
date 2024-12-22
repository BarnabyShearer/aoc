def aoc(data):
    map, moves = data.split("\n\n")
    map = list(map)
    D = {"<": -1, ">": +1, "^": -map.index("\n") - 1, "v": map.index("\n") + 1}
    p = map.index("@")
    for move in moves.replace("\n", ""):
        for i in range(1, 100):
            if map[p + i * D[move]] == ".":
                map[p] = "."
                if i > 1:
                    map[p + i * D[move]] = "O"
                p += D[move]
                map[p] = "@"
            elif map[p + i * D[move]] == "O":
                continue
            break
    total = 0
    for y, l in enumerate("".join(map).split("\n")):
        for x, c in enumerate(l):
            if c == "O":
                total += 100 * y + x
    return total
