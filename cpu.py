from collections import defaultdict


def cpu(data, input=[]):
    data = defaultdict(lambda: 0, enumerate([int(x) for x in data.split(",")]))
    for i, x in enumerate(input):
        data[i + 1] = x
    pc = 0
    base = 0
    mode = []

    def load(off):
        if mode[off] == 1:
            return data[pc + off]
        if mode[off] == 2:
            return data[base + data[pc + off]]
        return data[data[pc + off]]

    def store(off, value):
        if mode[off] == 1:
            data[pc + off] = value
        elif mode[off] == 2:
            data[base + data[pc + off]] = value
        else:
            data[data[pc + off]] = value

    while True:
        inst = int(f"{data[pc]}"[-2:])
        mode = [int(d) for d in f"{data[pc]:05}"[-2:-6:-1]]
        if inst == 99:
            if input:
                yield data[0]
            return
        if inst == 1:
            store(3, load(1) + load(2))
            pc += 4
        elif inst == 2:
            store(3, load(1) * load(2))
            pc += 4
        elif inst == 3:
            x = yield
            store(1, x)
            pc += 2
        elif inst == 4:
            yield load(1)
            pc += 2
        elif inst == 5:
            if load(1):
                pc = load(2)
            else:
                pc += 3
        elif inst == 6:
            if not load(1):
                pc = load(2)
            else:
                pc += 3
        elif inst == 7:
            store(3, int(load(1) < load(2)))
            pc += 4
        elif inst == 8:
            store(3, int(load(1) == load(2)))
            pc += 4
        elif inst == 9:
            base += load(1)
            pc += 2
        else:
            raise Exception(data[pc - 8 : pc])


def read(c):
    string_output = ""
    binary_output = []
    try:
        t = next(c)
        while t is not None:
            if t < 128:
                string_output += chr(t)
            else:
                binary_output.append(t)
            t = next(c)
    except StopIteration:
        pass
    return string_output, binary_output


def write(c, input):
    string_output = ""
    binary_output = []
    for a in input:
        string_output += a
        t = c.send(ord(a))
        if t is not None:
            if t < 128:
                string_output += chr(t)
            else:
                binary_output.append(t)
    a, b = read(c)
    return string_output + a, binary_output + b
