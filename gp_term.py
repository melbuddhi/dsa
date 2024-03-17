# geometric progression's Nth term
import time
import math
def term_of_gp(A, B, N):
    common_ratio = B / A
    progression_factor = math.pow(common_ratio, N - 1)
    return A * progression_factor

x,y,z = map(int, input("enter A B and N: ").split())
start_time=time.time()
print(term_of_gp(x,y,z))
end_time=time.time()
print(f"\n\ntime taken: {end_time-start_time: .8f}s")