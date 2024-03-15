def all_div(N):
    divisors = []
    i=1
    while i*i < N:
        if N%i==0:
            divisors.append(i)
        i+=1

    while i >= 1:
        if N % i == 0:
            divisors.append(int(N/i))
        i-=1
    return divisors


number = int(input("enter number:"))
print(all_div(number))