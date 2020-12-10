def two_sum(data, target=0):
    need = set()
    for n in data:
        if n in need:
            return n, target - n
        need.add(target - n)


def aoc(input):
    data = [int(n) for n in input.split("\n")]
    a, b = two_sum(data, 2020)
    return a * b
