from aoc20201202a import parse


def aoc(input):
    good = 0
    for [a, b], let, passwd in [parse(n) for n in input.split("\n")]:
        if (passwd[a - 1] == let) ^ (passwd[b - 1] == let):
            good += 1
    return good
