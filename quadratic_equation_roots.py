import time
import math


def func(a, b, c):
    roots = []
    if (b * b - 4 * a * c) < 0:
        roots.append("Imaginary roots")
        # the roots are complex numbers i.e. imaginary
    else:
        roots.append(int((-b + (math.sqrt(b * b - 4 * a * c))) // (2 * a)))
        roots.append(int((-b - math.sqrt((b * b - 4 * a * c))) // (2 * a)))

        if roots[1] >= roots[0]:
            temp = roots[0]
            roots[0] = roots[1]
            roots[1] = temp

    return roots


A, B, C = map(int, input("enter constants a b c of quadratic equation: ").split())
start_time = time.time()
print(func(A, B, C))
end_time = time.time()
print(f"\n\ntime taken: {end_time - start_time: .8f}s")
