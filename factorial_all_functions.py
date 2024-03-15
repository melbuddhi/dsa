import math  # only for counting digits of a factorial result


def find_factorial(num):
    # Space complexity is O(1) using while loop
    # result = 1
    # while num != 0:
    #     result *= num
    #     num -= 1
    # return result

    # Space complexity is O(n) using recursive function
    if num == 0:
        return 1
    return find_factorial(num - 1) * num


def digits_in_factorial(num):
    # We can't use above function for large N, to calculate factorial first & then use log.
    # Instead, we use one for loop like below:

    count = 1
    for i in range(1, num + 1):
        count += math.log(i, 10)
    return math.floor(count)


def find_trailing_zeroes(n):
    count = 0
    i = 5
    while n / i >= 1:
        count += int(n / i)
        i *= 5

    return int(count)


x = int(input("Enter number: "))
print(
    f"Factorial of {x} is {find_factorial(x)} and it has {digits_in_factorial(x)} digits. There are {find_trailing_zeroes(x)} zero (0) digits at the end.")
