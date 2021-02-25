# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt


def findfactors(x):
    list = []
    # x = math.sqrt(x)
    for i in range(2, int(sqrt(x))):
        if x % i == 0:
            list.append(i)
    return list


primes = []


def get_primes():
    factors = findfactors(600851475143)
    counter = 0
    for i in factors:
        for k in range(2, i):
            if i % k == 0:
                counter += 1
        if counter == 0:
            primes.append(i)
    return primes


def largest_prime():
    return max(get_primes())


print(largest_prime())
