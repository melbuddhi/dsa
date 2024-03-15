def prime_factor(num1):
    a = ''

    for i in range(2,num1+1):
        x = i
        if is_prime(i):
            while num1 % x == 0:
                a += str(i) + ' '
                x*=i


    return a

def is_prime(N):
    if N == 1:
        return False
    if N == 2 or N == 3:
        return True
    if N % 2 == 0 or N % 3 == 0:
        return False

    i = 5

    while (i*i <= N):
        if N % i == 0 or N % (i+2) == 0:
            return False
        i += 6

    return True
if __name__ == '__main__':
    a = 200
    print(prime_factor(a))