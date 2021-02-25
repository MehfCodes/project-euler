# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# -----------------------------------------------------------------------------------------------------------------------------------
# with numpy library and its lcm built-in method
import functools
import math
import numpy as np
arr = []
for i in range(1, 21):
    arr.append(i)
sm = np.lcm.reduce(arr)
print(sm)

# # ====================================================
# # another way:with math,functools library and lcm method that i implemented it by myself


def lcm(numbers):
    return functools.reduce(lambda a, b: int(a*b/math.gcd(a, b)), numbers)


print(lcm([i for i in range(1, 21)]))


# =========================================================
# implement lcm without any library but its useful for small nambers or two numbers
# send argumants as list (minimum length of list is 2)
def lcm_lcm(n):
    number = 1
    counter = 0
    while True:
        for i in n:
            if number % i == 0:
                counter += 1
            else:
                counter = 0
                number += 1
                break
        if counter == len(n):
            return number


print(lcm([i for i in range(1, 10)]))
