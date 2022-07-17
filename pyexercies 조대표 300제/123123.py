import string
from sys import stdin
a = stdin.readline().upper()
d = dict(zip(string.ascii_uppercase, [0]*26))

maxa: int = 0
last: str = '?'
flag: int = 0
for c in string.ascii_uppercase:
    d[c] = a.count(c)
    if d[c] > maxa:
        maxa = d[c]
        last = c
        flag = 0

    elif d[c] == maxa:
        flag += 1

print('?' if flag > 0 else last)