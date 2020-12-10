map = {
    1: {"D": 3},
    2: {"R": 3, "D": 6},
    3: {"R": 4, "D": 7},
    4: {"D": 8},
    5: {"R": 6},
    6: {"L": 7, "D": 0xA},
    7: {"L": 8, "D": 0xB},
    8: {"L": 9, "D": 0xC},
    9: {},
    0xA: {"L": 0xB},
    0xB: {"L": 0xC, "D": 0xD},
    0xC: {},
    0xD: {},
}


def aoc(data):
    for n, v in map.items():
        for nn, vv in map.items():
            for a, b in ("LR", "RL", "UD", "DU"):
                if n == vv.get(a):
                    v[b] = nn
    button = 5
    code = ""
    for line in data.split("\n"):
        for step in line:
            button = map[button].get(step, button)
        code += f"{button:X}"
    return code
