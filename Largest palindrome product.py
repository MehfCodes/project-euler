# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 � 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

stack = []


def max(args):
    max = 0
    for i in args:
        if max < i:
            max = i
    return max


def largest_palindrome():
    for x in range(100, 1001):
        for y in range(100, 1001):
            n = str(x*y)
            # print(n)
            new_list = list(n)
            # print(new_list)
            if len(new_list) >= 6:
                if new_list[0] == new_list[5] and new_list[1] == new_list[4] and new_list[2] == new_list[3]:
                    stack.append(int(''.join(new_list)))
            else:
                continue
    largest = max(stack)
    return largest


print(largest_palindrome())
