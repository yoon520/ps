import math

n = int(input())
num = []
for i in range(n):
    num.append(int(input()))

m = max(num)
tf = [False, False] + [True for i in range(2, m+1)]

for i in range(2, int(math.sqrt(m)+1)):
    if tf[i]:
        j = 2
        while i*j<=m:
            tf[i*j]=False
            j += 1

for i in num:
    q = i//2
    while tf[q] == False  or tf[i-q] == False:
        q -= 1
    print(q, i-q)