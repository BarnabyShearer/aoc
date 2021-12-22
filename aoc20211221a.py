def parse(data):
    return [int(l.split()[-1]) for l in data.split("\n")]


def to10(x):
    return (x - 1) % 10 + 1


def deterministic_die():
    while True:
        yield from range(1, 101)


def turn(die, start):
    return to10(start + next(die) + next(die) + next(die))


def game(die, players, target):
    score = [0] * len(players)
    roles = 0
    while True:
        for i, p in enumerate(players):
            players[i] = turn(die, p)
            roles += 3
            score[i] += players[i]
            if score[i] >= target:
                return roles, score


def aoc(data):
    roles, score = game(deterministic_die(), parse(data), 1000)
    return roles * min(score)
