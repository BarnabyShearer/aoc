from aoc20201207a import parse


def recurse(bags, target):
    return 1 + sum([recurse(bags, k) * v for k, v in bags[target].items()])


def aoc(data):
    return recurse(parse(data), "shiny gold") - 1
