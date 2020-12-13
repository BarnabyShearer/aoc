def pathfind(maze, start, target):
    seen = set(((target, 0),))
    q = [
        (1, target, 0),
    ]
    while q:
        steps, prev, z = q.pop(0)
        for pos, dz in maze[prev]:
            if z + dz < 0 or (pos, z + dz) in seen:
                continue
            if z + dz == 0 and pos == start:
                return steps
            seen.add((pos, z + dz))
            q.append((steps + 1, pos, z + dz))


def aoc(data):
    w = data.index("\n") + 1
    map = [-w, -1, 1, w]
    warp = {}
    for pos, square in enumerate(data):
        if square == ".":
            for dir in map:
                p = pos + dir
                if 0 <= p < len(data) and data[p] != "#" and data[p] != ".":
                    warp.setdefault(frozenset((data[p], data[p + dir])), []).append(pos)
    maze = {}
    for pos, square in enumerate(data):
        if square == ".":
            for dir in map:
                p = pos + dir
                if 0 <= p < len(data) and data[p] != "#":
                    z = 0
                    if data[p] != ".":
                        for w in warp[frozenset((data[p], data[p + dir]))]:
                            if w != pos:
                                if (
                                    p + dir + dir < 0
                                    or p + dir + dir > len(data)
                                    or data[p + dir + dir] == "\n"
                                ):
                                    z = -1
                                else:
                                    z = 1
                                p = w
                                break
                        else:
                            continue
                    maze.setdefault(pos, []).append((p, z))
    return pathfind(maze, warp[frozenset("AA")][0], warp[frozenset("ZZ")][0])
