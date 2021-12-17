def parse(data):
    return "".join(f"{b:08b}" for b in bytes.fromhex(data))


def packets(data, process=None, max=99999):
    for _ in range(max):
        if not data or not int(data, 2):
            break
        ver = int(data[:3], 2)
        match int(data[3:6], 2), data[6]:
            case 4, _:
                val = 0
                i = 6
                while True:
                    val *= 16
                    val += int(data[i + 1 : i + 5], 2)
                    i += 5
                    if data[i - 5] == "0":
                        break
                yield (ver, 4, val, i)
                data = data[i:]
            case op, "1":
                num = int(data[7:18], 2)
                sub = list(packets(data[18:], process, num))
                sub_len = sum(i for _, __, ___, i in sub)
                yield process(ver, op, sub, 18 + sub_len)
                data = data[18 + sub_len :]
            case op, "0":
                length = int(data[7:22], 2)
                yield process(
                    ver, op, packets(data[22 : 22 + length], process), 22 + length
                )
                data = data[22 + length :]


def sum_ver(ver, op, sub, length):
    return (
        ver + sum(ver for ver, _, __, ___ in sub),
        op,
        sub,
        length,
    )


def aoc(data):
    return next(packets(parse(data), sum_ver))[0]
