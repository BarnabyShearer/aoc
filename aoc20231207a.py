def parse(data):
    return [(l.split()[0], int(l.split()[1])) for l in data.split("\n")]


def score_hand(hand):
    if len(set(hand)) == 1:
        return 7
    elif len(set(hand)) == 2:
        if hand.count(hand[0]) in (1, 4):
            return 6
        else:
            return 5
    elif len(set(hand)) == 3:
        if any(hand.count(hand[x]) == 3 for x in range(3)):
            return 4
        else:
            return 3
    elif len(set(hand)) == 4:
        return 2
    return 1


def score(hand):
    total = score_hand(hand)
    for c in hand:
        total *= 13
        total += "23456789TJQKA".index(c)
    return total


def win(data, score):
    ranked = enumerate(sorted(parse(data), key=lambda h: score(h[0])))
    return sum(bid * (rank + 1) for rank, (_, bid) in ranked)


def aoc(data):
    return win(data, score)
