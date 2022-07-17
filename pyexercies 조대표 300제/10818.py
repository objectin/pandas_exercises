from sys import stdin

c = int(stdin.readline())
for line in stdin:
    n, *l = map(int, line.strip().split())
    avg = sum(l) / n
    per = sum([1 for i in l if i > avg]) / n * 100
    
    print(f'{per:.3f}%')


count = 0
    for i in l:
        if i > avg:
            count += 1

    per = count / n * 100