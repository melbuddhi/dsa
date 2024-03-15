def count_prime_squares(N):
    i = 2
    val = 0
    while i*i<=N:
        j = 2
        while j*j <= i:
            if i % j == 0:
                val -= 1
                break
            j += 1
        val += 1
        i += 1

    print(val)

num = 300
print(count_prime_squares(num))