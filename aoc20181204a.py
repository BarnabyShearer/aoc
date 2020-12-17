def get_sleeps(data):
    guards = {}
    guard = None
    for line in sorted(data.split("\n")):
        if "Guard" in line:
            guard = int(line.split()[3][1:])
        elif "asleep" in line:
            guards.setdefault(guard, []).append([int(line.split()[1][3:5]), 0])
        else:
            guards[guard][-1][1] = int(line.split()[1][3:5])
    return guards


def aoc(data):
    guards = get_sleeps(data)
    max = 0
    max_guard = None
    for guard, times in guards.items():
        total = sum([s[1] - s[0] for s in times])
        if total > max:
            max = total
            max_guard = guard
    max = 0
    max_m = None
    for m in range(60):
        total = 0
        for time in guards[max_guard]:
            if time[0] <= m < time[1]:
                total += 1
        if total > max:
            max = total
            max_m = m
    return max_guard * max_m
