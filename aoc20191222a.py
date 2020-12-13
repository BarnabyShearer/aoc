def shuffle(data, deck):
    for line in data.split("\n"):
        f, *_, l = line.split()
        if l == "stack":
            deck.reverse()
        elif f == "cut":
            deck = deck[int(l) :] + deck[: int(l)]
        else:
            for i, d in enumerate(deck.copy()):
                deck[(i * int(l)) % len(deck)] = d
    return deck


def aoc(data):
    return shuffle(data, list(range(10007))).index(2019)
