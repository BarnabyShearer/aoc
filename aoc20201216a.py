def parse_tickets(tickets):
    return (
        tuple(int(t) for t in ticket.split(",")) for ticket in tickets.split("\n")[1:]
    )


def parse(data):
    rules = []
    rules_string, my, near = data.split("\n\n")
    for rule in rules_string.split("\n"):
        _, values = rule.split(":")
        rule = []
        for range in values.split(" or "):
            rule.append(tuple(int(a) for a in range.split("-")))
        rules.append(rule)
    return rules, next(parse_tickets(my)), parse_tickets(near)


def aoc(data):
    rules, _, near = parse(data)
    total = 0
    for ticket in near:
        for value in ticket:
            for rule in rules:
                for range in rule:
                    if range[0] <= value <= range[1]:
                        break
                else:
                    continue
                break
            else:
                total += value
    return total
