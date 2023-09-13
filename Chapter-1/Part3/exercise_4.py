import random


def main():
    chance = random.random()
    print(chance)

    if chance < 0.80:
        favourite = "dogs"
    elif chance > 0.80 and chance < 0.90:
        favourite = "cats"
    elif chance > 0.90:
        favourite = "bats"

    print("I love " + favourite)


main()
