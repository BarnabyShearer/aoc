def aoc(data):
    map, moves = data.split("\n\n")
    map = map.replace("#", "##")
    map = map.replace("O", "[]")
    map = map.replace(".", "..")
    p = map.index("@")
    map = map.replace("@", "@.")
    map = list(map)
    D = {"<": -1, ">": +1, "^": -map.index("\n") - 1, "v": map.index("\n") + 1}
    for move in moves.replace("\n", ""):
        ok = True
        oldmap = map.copy()
        p = map.index("@")
        moving = set([p + D[move]])
        while ok and moving:
            n = set()
            for m in moving:
                if map[m] == "#":
                    ok = False
                    break
                else:
                    if map[m] in "[]":
                        n.add(m + D[move])
                        if move in "^v":
                            n.add(m + D[move] + D["<" if map[m] == "]" else ">"])
                            map[m + D["<" if map[m] == "]" else ">"]] = (
                                oldmap[m - D[move] + D["<" if map[m] == "]" else ">"]]
                                if m - D[move] + D["<" if map[m] == "]" else ">"]
                                in moving
                                else "."
                            )
                    map[m] = oldmap[m - D[move]]
            moving = n
        map[p] = "."
        map[p + D[move]] = "@"
        if not ok:
            map = oldmap
    total = 0
    for y, l in enumerate("".join(map).split("\n")):
        for x, c in enumerate(l):
            if c == "[":
                total += 100 * y + x
    return total
