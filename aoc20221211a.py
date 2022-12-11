def monkey(data):
    _, items, op, test, t, f = (i.split(":")[1] for i in data.split("\n"))
    items = [int(i) for i in items.split(", ")]
    op = op.split("= ")[1]
    test, t, f = (int(i.split()[-1]) for i in (test, t, f))
    return [items, op, test, t, f, 0]


def parse(data):
    return [monkey(m) for m in data.split("\n\n")]


def game(monkeys, rounds=20, calm=lambda x: x // 3):
    for _ in range(rounds):
        for m in monkeys:
            while m[0]:
                i = m[0].pop(0)
                m[5] += 1
                n = calm(eval(m[1].replace("old", str(i))))
                monkeys[m[3] if n % m[2] == 0 else m[4]][0].append(n)
    seen = sorted(m[5] for m in monkeys)
    return seen[-2] * seen[-1]


def aoc(data):
    return game(parse(data))
