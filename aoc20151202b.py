from aoc20151202a import parse


def ribbon(w, l, h):
    size = [l + w, w + h, h + l]
    return w * l * h + min(size) * 2


def aoc(data):
    return sum([ribbon(*parse(line)) for line in data.split("\n")])
