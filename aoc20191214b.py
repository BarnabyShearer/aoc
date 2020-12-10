from aoc20191214a import formular, need


def aoc(data):
    form = formular(data)
    start = 2
    end = 100000000000
    while True:
        test = start + (end - start) // 2
        ore = need(form, {"FUEL": test})["ORE"]
        if ore <= 1000000000000:
            ore = need(form, {"FUEL": test + 1})["ORE"]
            if ore > 1000000000000:
                return test
            start = test
        if ore > 1000000000000:
            end = test
