import math


def calculate_hypotenuse(base, height):
    hypotenuse = math.sqrt(base ** 2 + height ** 2)
    print("Hypotenuse is {}".format(hypotenuse))


def main():
    base = float(input("Enter the base:"))
    height = float(input("Enter the height:"))
    calculate_hypotenuse(base, height)


main()
