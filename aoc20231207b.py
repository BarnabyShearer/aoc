from aoc20231207a import win, score_hand

CARDS = "J23456789TQKA"


def score(hand):
    total = max(score_hand(hand.replace("J", c)) for c in CARDS[1:])
    for c in hand:
        total *= 13
        total += CARDS.index(c)
    return total


def aoc(data):
    return win(data, score)
