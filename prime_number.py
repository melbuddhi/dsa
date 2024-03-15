def prime(N):

    # if N == 1:
    #     return False
    # else:
    #     for i in range(2, N):
    #         if N % i == 0:
    #             return False
    #         else:
    #             return True

    # efficient method:

    # if N == 1:
    #     return False
    # i = 2
    #
    # while i*i <= N:
    #     if N % i == 0:
    #         return False
    #     i+=1
    #
    # return True

    # super efficient method:

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
    a = 37
    print(prime(a))
