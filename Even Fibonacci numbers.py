# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

s1 = 1
s2 = 2
s3 = s1+s2

n = 4000000
counter = 2
sum = 2
print(s1, s2)
while(s3 < n):
    if s3 % 2 == 0:
        sum = sum+s3
    s1 = s2
    s2 = s3
    s3 = s1+s2
print(sum)
