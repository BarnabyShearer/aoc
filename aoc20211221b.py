from collections import Counter
from copy import copy

from aoc20211221a import *

DIRAC_DIE = Counter(
    sum((x, y, z)) for x in range(1, 4) for y in range(1, 4) for z in range(1, 4)
)


def dirac_game(score, players, target):
    wins = [0] * len(players)
    for d0, u0 in DIRAC_DIE.items():
        if score[0] + to10(players[0] + d0) >= target:
            wins[0] += u0
        else:
            for d1, u1 in DIRAC_DIE.items():
                if score[1] + to10(players[1] + d1) >= target:
                    wins[1] += u0 * u1
                else:
                    nscore = copy(score)
                    nplayers = copy(players)
                    nplayers[0] = to10(nplayers[0] + d0)
                    nscore[0] += nplayers[0]
                    nplayers[1] = to10(nplayers[1] + d1)
                    nscore[1] += nplayers[1]
                    nwins = dirac_game(nscore, nplayers, 21)
                    wins[0] += u0 * u1 * nwins[0]
                    wins[1] += u0 * u1 * nwins[1]
    return wins


def aoc(data):
    players = parse(data)
    wins = dirac_game([0] * len(players), players, 21)
    return max(wins)
