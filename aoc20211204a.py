from operator import itemgetter


def parse(data):
    game, *boards = data.split("\n\n")
    return [int(m) for m in game.split(",")], [
        [[int(c) for c in r.split()] for r in b.split("\n")] for b in boards
    ]


def T(m):
    return list(map(list, zip(*m)))


def turns(game, board):
    return min(max(game.index(c) for c in r) for r in board + T(board)) + 1


def best(game, boards, op):
    return op(((b, turns(game, b)) for b in boards), key=itemgetter(1))


def score(game, board):
    return sum(c for r in board for c in r if c not in game) * game[-1]


def calc(data, op):
    game, boards = parse(data)
    board, length = best(game, boards, op)
    return score(game[:length], board)


def aoc(data):
    return calc(data, min)
