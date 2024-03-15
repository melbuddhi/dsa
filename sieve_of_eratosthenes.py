import time
start_time = time.time()
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

def func(N):
    start_time = time.time()
    if N == 1:
        return
    is_prime_array = [True]*(N+1)
    i = 2

    while i*i <= N:
        if is_prime(i):
            for j in range(i*i, N+1, i):
                is_prime_array[j] = False
        i+=1

    for i in range(2, N+1):
        if is_prime_array[i]:
            print(i, end = " ")
    end_time=time.time()
    print(f"\n\n------\ntime take: {end_time-start_time} seconds")

x = int(input("enter number: "))
func(x)
