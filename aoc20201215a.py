def aoc(data):
    said = [int(n) for n in data.split(",")]
    for i in range(len(said), 2020):
        try:
            said.append(said[-2::-1].index(said[-1]) + 1)
        except ValueError:
            said.append(0)
    return said[-1]
