from aoc20201221a import has_allergen


def aoc(data):
    return ",".join("".join(x) for _, x in sorted(has_allergen(data).items()))
