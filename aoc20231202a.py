from collections import defaultdict


def parse(data):
    for line in data.split("\n"):
        game, res = line.split(":")
        yield int(game[5:]), tuple(
            defaultdict(
                lambda: 0, {c.split(" ")[2]: int(c.split(" ")[1]) for c in s.split(",")}
            )
            for s in res.split(";")
        )


def aoc(data):
    total = 0
    for game, res in parse(data):
        if all(s["red"] <= 12 and s["green"] <= 13 and s["blue"] <= 14 for s in res):
            total += game
    return total
