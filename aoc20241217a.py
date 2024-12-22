def parse(data):
    data, prog = data.split("\n\n")
    A, B, C = (int(i.split(": ")[-1]) for i in data.split("\n"))
    prog = list(int(i) for i in prog.split(": ")[-1].split(","))
    return prog, A, B, C


def cpu(prog, A, B, C):
    def combo(v):
        match v:
            case 4:
                return A
            case 5:
                return B
            case 6:
                return C
            case 7:
                raise Exception()
            case _:
                return v

    p = 0
    while True:
        if p >= len(prog):
            break
        op = prog[p]
        v = prog[p + 1]
        match op:
            case 0:  # adv
                A = A // 2 ** combo(v)
            case 1:  # bxl
                B ^= v
            case 2:  # bst
                B = combo(v) % 8
            case 3:  # jnz
                if A:
                    p = v - 2
            case 4:  # bxc
                B = B ^ C
            case 5:  # out
                yield combo(v) % 8
            case 6:  # bdv
                B = A // 2 ** combo(v)
            case 7:  # cdv
                C = A // 2 ** combo(v)
        p += 2


def aoc(data):
    return ",".join(str(i) for i in cpu(*parse(data)))
