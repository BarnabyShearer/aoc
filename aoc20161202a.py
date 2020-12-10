map = {
    "U": (-3, []),
    "D": (+3, []),
    "L": (-1, [4, 7]),
    "R": (+1, [3, 6]),
}


def aoc(data):
    button = 5
    code = ""
    for line in data.split("\n"):
        for step in line:
            new = button + map[step][0]
            if 0 < new <= 9 and not button in map[step][1]:
                button = new
        code += str(button)
    return code
