# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import itertools
from math import sqrt

# import datetime
# start = datetime.datetime.now()


def is_prime(x):
    for i in range(2, int(sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


def nth_prime(n):
    nth = 0
    for i in itertools.count(2):
        if is_prime(i):
            nth += 1
        if nth == n:
            # print(nth, n)
            return i


print(nth_prime(10001))
# print(is_prime())
# end = datetime.datetime.now()
# print(end-start)
