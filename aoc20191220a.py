def pathfind(maze, start, target):
    path = {target: 0}
    i = 0
    while start not in path:
        prev = list(path.keys())[i]
        for pos in maze[prev]:
            path[pos] = min(path.get(pos, path[prev] + 1), path[prev] + 1)
        i += 1
    return path


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
                    if data[p] != ".":
                        for w in warp[frozenset((data[p], data[p + dir]))]:
                            if w != pos:
                                p = w
                                break
                        else:
                            continue
                    maze.setdefault(pos, []).append(p)
    return pathfind(maze, warp[frozenset("AA")][0], warp[frozenset("ZZ")][0])[
        warp[frozenset("AA")][0]
    ]
