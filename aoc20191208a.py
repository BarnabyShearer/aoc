def layers(data):
    return list(zip(*[iter([int(x) for x in data])] * 25 * 6))


def aoc(data):
    min = 999999
    total = 0
    for layer in layers(data):
        if layer.count(0) < min:
            min = layer.count(0)
            total = layer.count(1) * layer.count(2)
    return total
