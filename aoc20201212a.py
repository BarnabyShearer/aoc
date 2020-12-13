def aoc(data):
    x, y, d = 0, 0, 0
    moves = {
        "E": (1, 0, 0),
        "S": (0, 1, 0),
        "W": (-1, 0, 0),
        "N": (0, -1, 0),
        "R": (0, 0, 1),
        "L": (0, 0, -1),
    }
    for move, step in [(i[0], int(i[1:])) for i in data.split()]:
        if move == "F":
            x += list(moves.values())[d // 90 % 4][0] * step
            y += list(moves.values())[d // 90 % 4][1] * step
        else:
            x += moves[move][0] * step
            y += moves[move][1] * step
            d += moves[move][2] * step
    return abs(x) + abs(y)
