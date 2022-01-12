import math


def add(num1, num2):
    print(num1 + num2)


def subtract(num1, num2):
    print(num1 + num2)


def multiply(num1, num2):
    print(num1 * num2)


def divide(num1, num2):
    print(num1 / num2)


def calculate_hypotenuse(base, height):
    hypotenuse = math.sqrt(base ** 2 + height ** 2)
    print("Hypotenuse is {}".format(hypotenuse))


def main():
    print("""
    1. to calculate hypotenuse
    2. to add
    3. to subtract
    4. to multiply
    5. to divide""")
    user_input = int(input())
    input_num1 = float(input("enter first number:"))
    input_num2 = float(input("enter second number:"))

    if user_input == 1:
        calculate_hypotenuse(input_num1, input_num2)
    elif user_input == 2:
        add(input_num1, input_num2)
    elif user_input == 3:
        subtract(input_num1, input_num2)
    elif user_input == 4:
        multiply(input_num1, input_num2)
    elif user_input == 5:
        divide(input_num1, input_num2)
    else:
        print("Invalid input")


main()
