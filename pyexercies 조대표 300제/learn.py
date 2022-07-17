# a + b * n < c * n
# a < (c-b) * n

import math

# 더해서 2인 분수 -> 1개
# 더해서 3인 분수 -> 2개
# 더해서 n+1인 분수 -> n개
# (1 + (n-1)) * (n-1) / 2 = n * (n-1) / 2

from sys import stdin

x = int(stdin.readline())
i = 1
sum = 0

# n - 1까지 구함
while True:
    if int(((i + 1) * (i + 2)) / 2) > x:
        #print(f'broke in {i}'    )
        sum = int((i * (i + 1)) / 2)
        break
    
    i += 1

k = i + 1
a = x - sum + 1
b = k - a
print(f'{a}/{b}')