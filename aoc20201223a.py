def aoc(data):
    cups = tuple(int(c) for c in data)
    for _ in range(100):
        dest = cups[0]
        while dest in cups[:4]:
            dest -= 1
            if dest == 0:
                dest = len(cups)
        dest = cups.index(dest) + 1
        cups = cups[4:dest] + cups[1:4] + cups[dest:] + cups[:1]
    return int(
        "".join(
            str(cups[(cups.index(1) + 1 + ii) % len(cups)])
            for ii in range(len(cups) - 1)
        )
    )
