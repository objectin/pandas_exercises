import collections

my_str = input().strip()
counter = collections.Counter(my_str)

max = -1
a = set()
for key, value in counter.items():
    if value >= max:
        max = value
        a.add(key)

