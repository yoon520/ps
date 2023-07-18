import math

s, e = map(int, input().split())
l = [False, False] + [True for i in range(1,e)]

for i in range(2, int(math.sqrt(e)+1)):
    if l[i]:
        j = 2
        while i*j <= e:
            l[i*j] = False
            j += 1

for i in range(s, e+1):
    if l[i]:
        print(i)