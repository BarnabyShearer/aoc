def aoc(data):
    cups = tuple(int(c) for c in data) + tuple(range(10, 1000001))
    nextcup = {}
    last = None
    for cup in cups:
        if last:
            nextcup[last] = cup
        last = cup
    nextcup[last] = cups[0]
    cup = cups[0]
    for _ in range(10000000):
        dest = cup
        while dest in (
            cup,
            nextcup[cup],
            nextcup[nextcup[cup]],
            nextcup[nextcup[nextcup[cup]]],
        ):
            dest -= 1
            if dest == 0:
                dest = len(cups)
        tmp = nextcup[cup]
        nextcup[cup] = nextcup[nextcup[nextcup[nextcup[cup]]]]
        nextcup[nextcup[nextcup[tmp]]] = nextcup[dest]
        nextcup[dest] = tmp
        cup = nextcup[cup]
    return nextcup[1] * nextcup[nextcup[1]]
