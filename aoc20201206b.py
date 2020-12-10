import string


def aoc(data):
    total = 0
    for group in data.split("\n\n"):
        all = set(string.ascii_lowercase)
        for person in group.split():
            all = all.intersection(person)
        total += len(all)
    return total
