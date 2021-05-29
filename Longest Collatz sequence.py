import time
start = time.time()
values = {1: 1}


def countChain(n):
    if n in values:
        return values[n]
    if n % 2 == 0:
        values[n] = 1 + countChain(n / 2)
    else:
        values[n] = 2 + countChain((3 * n + 1) / 2)

    return values[n]


longest_chain = 0
answer = -1

for i in range(500000, 1000000):
    if countChain(i) > longest_chain:
        longest_chain = countChain(i)
        answer = i


print(answer)
print('Time:', 1000*(time.time() - start))
