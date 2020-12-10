import math


def parse(x):
    return int(x.split()[0]), x.split()[1]


def formular(data):
    result = {}
    for reaction in data.split("\n"):
        r, p = reaction.split("=>")
        a, c = p.split()
        result[c] = (int(a), [parse(x) for x in r.split(",")])
    return result


def need(form, state):
    more = True
    while more:
        more = False
        for key, value in state.copy().items():
            if key != "ORE":
                if value > 0:
                    mul = math.ceil(value / form[key][0])
                    state[key] -= mul * form[key][0]
                    for n, id in form[key][1]:
                        state.setdefault(id, 0)
                        state[id] += n * mul
                    more = True
    return state


def aoc(data):
    return need(formular(data), {"FUEL": 1})["ORE"]
