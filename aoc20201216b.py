from aoc20201216a import parse


def aoc(data):
    rules, my, near = parse(data)

    matches = []
    for ticket in near:
        matches.append([])
        for value in ticket:
            matches[-1].append(set())
            for i, rule in enumerate(rules):
                for rulerange in rule:
                    if rulerange[0] <= value <= rulerange[1]:
                        matches[-1][-1].add(i)
                        break

    posible = [set(range(len(rules))) for _ in rules]
    for ticket in matches:
        if all(ticket):
            for i, field in enumerate(ticket):
                posible[i] &= field

    done = {}
    while len(done) < len(rules):
        for i in range(len(rules)):
            if i not in done:
                options = [ii for ii, p in enumerate(posible) if i in p]
                if len(options) == 1:
                    done[i] = options[0]
                    posible[options[0]] = set()

    return (
        my[done[0]]
        * my[done[1]]
        * my[done[2]]
        * my[done[3]]
        * my[done[4]]
        * my[done[5]]
    )
