import math


def count_digits(x):
    # Using log, instead of a loop
    return math.floor(math.log(x, 10)) + 1


x = int(input("Enter the number: "))
print(f"In the number `{x}` there are {count_digits(x)} digit(s)")