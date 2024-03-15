import time


def func(num, pow):
    temp = 0

    if pow == 0:
        return 1

    temp = func(num, pow // 2)
    temp *= temp

    if pow % 2 == 0:
        return temp
    else:
        return temp * num


x, y = map(int, input("enter numbers: ").split())
start_time=time.time()
print(func(x,y))
end_time=time.time()
print(f"\n\ntime taken: {end_time-start_time: .8f}s")