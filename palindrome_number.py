def is_palindrome(x):
    temp = x
    rev = 0

    while temp != 0:
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10

    return rev == x


num = int(input("Enter number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
