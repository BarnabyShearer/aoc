def aoc(data):
    data = data.split("\n")
    for i, line in enumerate(data):
        for line2 in data[i + 1 :]:
            for ii in range(len(line)):
                if line[:ii] + line[ii + 1 :] == line2[:ii] + line2[ii + 1 :]:
                    return line[:ii] + line[ii + 1 :]
