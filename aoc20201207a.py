def parse(data):
    bags = {}
    for line in data.replace(" bags", "").replace(" bag", "").split("\n"):
        a, b = line[:-1].split(" contain ")
        if "no other" in b:
            bags[a] = {}
        else:
            bags[a] = {
                bb.split(maxsplit=1)[1]: int(bb.split(maxsplit=1)[0])
                for bb in b.split(",")
            }
    return bags


def aoc(data):
    bags = parse(data)
    options = set(["shiny gold"])
    while True:
        prev = len(options)
        for bag in options.copy():
            for outer, inner in bags.items():
                if bag in inner.keys():
                    options.add(outer)
        if prev == len(options):
            break
    return len(options) - 1
