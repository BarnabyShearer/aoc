PAIR = {"(": ")", "[": "]", "{": "}", "<": ">"}


def parse(data):
    return data.split("\n")


def p(line):
    need = ""
    for c in line:
        if c in PAIR:
            need += PAIR[c]
        elif c == need[-1]:
            need = need[:-1]
        else:
            return True, c
    return False, reversed(need)


def score(msg):
    return {")": 3, "]": 57, "}": 1197, ">": 25137}[msg]


def aoc(data):
    return sum(score(m) for s, m in (p(l) for l in parse(data)) if s)
