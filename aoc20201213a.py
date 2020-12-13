def aoc(data):
    t, buses = data.split()
    t = int(t)
    best = 0
    min = 999999999999
    for bus in [int(b) for b in buses.split(",") if b != "x"]:
        wait = bus - t % bus
        if wait < min:
            min = wait
            best = bus
    return best * min
