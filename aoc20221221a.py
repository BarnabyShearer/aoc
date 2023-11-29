def parse(data):
    return {l.split(":")[0]: l.split(":")[1][1:] for l in data.split("\n")}


def order(lookup):
    seen = set()
    code = ""
    for k, v in lookup.items():
        if all(op not in v for op in "+-*/"):
            seen.add(k)
            code += f"{k} = {v}\n"
    while lookup.keys() - seen:
        for k, v in lookup.items():
            if k in seen:
                continue
            a, op, b = v.split()
            if a in seen and b in seen:
                seen.add(k)
                code += f"{k} = {v}\n"
    return code


def aoc(data):
    exec(order(parse(data)), globals())
    return int(root)
