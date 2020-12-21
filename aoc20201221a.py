import copy


def parse(data):
    yield from (
        (x.replace(",", "").split() for x in dish[:-1].split(" (contains "))
        for dish in data.split("\n")
    )


def has_allergen(data):
    avoid = {}
    for ingredients, allergens in parse(data):
        for allergen in allergens:
            if allergen in avoid:
                avoid[allergen] = avoid[allergen].intersection(ingredients)
            else:
                avoid[allergen] = set(ingredients)

    while any(len(ingredients) != 1 for ingredients in avoid.values()):
        for allergen in avoid:
            if len(avoid[allergen]) == 1:
                ingredient = tuple(avoid[allergen])[0]
                for notallergen in avoid:
                    if allergen != notallergen and ingredient in avoid[notallergen]:
                        avoid[notallergen].remove(ingredient)
    return avoid


def aoc(data):

    bad = set()
    for avoid in has_allergen(data).values():
        bad |= avoid

    total = 0
    for ingredients, _ in parse(data):
        for ingredient in ingredients:
            if ingredient not in bad:
                total += 1

    return total
