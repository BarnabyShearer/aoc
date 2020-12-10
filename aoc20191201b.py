def recurse(mass):
    newmass = mass // 3 - 2
    if newmass > 0:
        return newmass + recurse(newmass)
    return 0


def aoc(data):
    return sum([recurse(int(x)) for x in data.split("\n")])
