from aoc20231202a import *


def aoc(data):
    total = 0
    for game, res in parse(data):
        total += (
            max(r["red"] for r in res)
            * max(r["green"] for r in res)
            * max(r["blue"] for r in res)
        )
    return total
