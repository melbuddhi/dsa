def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


# efficient way to find lcm:
def lcm(num1, num2):
    return num1 * num2 // gcd(num1, num2)


if __name__ == '__main__':
    a = 13
    b = 2
    print(f"HCF={gcd(a, b)} and LCM={lcm(a, b)}")
