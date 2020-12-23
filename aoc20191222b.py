def aoc(data):
    length = 119315717514047
    it = 101741582076661
    a, b = 1, 0
    for line in data.split("\n"):
        f, *_, l = line.split()
        if l == "stack":
            aa, bb = -1, -1
        elif f == "cut":
            aa, bb = 1, -int(l)
        else:
            aa, bb = int(l), 0
        a = (aa * a) % length
        b = (aa * b + bb) % length

    ma = pow(a, it, length)
    mb = (b * (ma - 1) * pow(a - 1, length - 2, length)) % length
    return ((2020 - mb) * pow(ma, length - 2, length)) % length
