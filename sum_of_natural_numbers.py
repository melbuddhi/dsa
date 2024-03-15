def sum_of(n):
    return n * (n + 1) // 2


n = int(input("Enter N: "))
print(f"The sum of natural numbers till {n} is {sum_of(n)}")
