# from math import sqrt, pow
# import datetime


# # def sumPrimes(n):
# #     sum, sieve = 0, [True] * n
# #     for p in range(2, n):
# #         if sieve[p]:
# #             sum += p
# #             for i in range(p*p, n, p):
# #                 sieve[i] = False
# #     return sum


# # print(sumPrimes(2000000))

# # start = datetime.datetime.now()
# # # my code


# # def is_prime(x):
# #     for i in range(2, int(sqrt(x)+1)):
# #         if x % i == 0:
# #             return False
# #     return True


# # def sum_of_pn_below(n):
# #     sum = 0
# #     for i in range(2, n):
# #         if is_prime(i):
# #             sum += i
# #     return sum


# # print(sum_of_pn_below(2000000))
# # end = datetime.datetime.now()


# # print(end - start)
# for a in range(1, 1000):
#     for b in range(1, 1000):
#         if a < b:
#             for c in range(1, 1000):
#                 if b < c:
#                     result = a+b+c
#                     if result == 1000:
#                         a2 = pow(a, 2)
#                         b2 = pow(b, 2)
#                         c2 = pow(c, 2)
#                         if a2+b2 == c2:
#                             abc = a*b*c
#                             print(abc)
#                 else:
#                     continue
#         else:
#             continue


# def is_dev_pytha(a, b, c):
#     if pow(a, 2)+pow(b, 2) == pow(c, 2):
#         return True
#     else:
#         False

from math import sqrt, pow

# my code


def sum_of_pn_below(n):
    # stack = []
    sum = 0
    for i in range(2, n+1):
        counter = 0
        for k in range(2, int(sqrt(i))):
            if i % k == 0:
                counter += 1
        if counter == 0:
            sum += i
    #         print(i)
    #         stack.append(i)
    # for x in stack:
    #     sum += x
    return sum


print(sum_of_pn_below(2000000))

for a in range(1, 1000):
    for b in range(1, 1000):
        if a < b:
            for c in range(1, 1000):
                if b < c:
                    result = a+b+c
                    if result == 1000:
                        a2 = pow(a, 2)
                        b2 = pow(b, 2)
                        c2 = pow(c, 2)
                        if a2+b2 == c2:
                            abc = a*b*c
                            print(abc)
                else:
                    continue
        else:
            continue


def is_dev_pytha(a, b, c):
    if pow(a, 2)+pow(b, 2) == pow(c, 2):
        return True
    else:
        False
