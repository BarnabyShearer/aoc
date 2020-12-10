from aoc20191208a import layers


def aoc(data):
    img = [-1] * 25 * 6
    for layer in layers(data):
        for i, pixel in enumerate(layer):
            if pixel != 2 and img[i] == -1:
                img[i] = pixel
    for row in list(zip(*[iter(img)] * 25)):
        print("".join(["█" if p else " " for p in row]))
    return input("please type what you see: ")
