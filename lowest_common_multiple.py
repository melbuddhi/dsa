def lcm(num1, num2):
    res = max(num1, num2)
    while True:
        if res % num1 == 0 and res % num2 == 0:
            return res
        res += 1


if __name__ == '__main__':
    a = 13
    b = 2
    print(lcm(a, b))
