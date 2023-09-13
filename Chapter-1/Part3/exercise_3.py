import math
import random  # just for generating random mountains

# generate random mountains

w = [0.05, random.random() / 3, random.random() / 3]
h = [
    1.0
    + math.sin(1 + x / 0.6) * w[0]
    + math.sin(-0.3 + x / 9.0) * w[1]
    + math.sin(-0.2 + x / 30.0) * w[2]
    for x in range(100)
]


def climb(x, h):
    summit = False

    while not summit:
        summit = True

        for offset in range(1, 6):
            if h[x + offset] > h[x]:
                x += offset
                summit = False
                break

        if summit:
            for offset in range(1, 6):
                if h[x - offset] > h[x]:
                    x -= offset
                    summit = False
                    break

    return x


def main(h):
    # start at a random place
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    print("final print: ", x0, x)
    return x0, x


main(h)
