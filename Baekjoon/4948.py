import math

arr =[]

while True:
    n = int(input())
    if n == 0:
        break
    else:
        arr.append(n)

max = max(arr)*2
tf = [False, False] + [True for i in range(max-1)]

for i in range(2,int(math.sqrt(max)+1)):
    if tf[i]:
        j = 2
        while i*j<=max:
            tf[i*j] = False
            j += 1

for i in arr:
    cnt = 0
    for j in range(i+1, 2*i+1):
        if tf[j]==True:
            cnt += 1
    print(cnt)