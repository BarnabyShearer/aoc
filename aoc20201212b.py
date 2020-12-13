def aoc(data):
    x, y, wx, wy = 0, 0, 10, -1
    moves = {"E": (1, 0), "S": (0, 1), "W": (-1, 0), "N": (0, -1)}
    for move, step in [(i[0], int(i[1:])) for i in data.split()]:
        if move in moves:
            wx += moves[move][0] * step
            wy += moves[move][1] * step
        elif move == "F":
            x += wx * step
            y += wy * step
        elif move == "L":
            move = "R"
            step = 360 - step
        if move == "R":
            for _ in range(step // 90 % 4):
                t = wx
                wx = -wy
                wy = t
    return abs(x) + abs(y)
