import sys

m = 1000000
tf = [False, False]+[True]*(m-1)
for i in range(2, 1001):
    if tf[i]:
        tf[i+i::i] = [0] * len(tf[i+i::i])

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    
    check = 0
    for i in range(3, n//2+1, 2):
        if tf[i] and tf[n-i]:
            print(f"{n} = {i} + {n-i}")
            check = 1
            break
    if check == 0:
        print("Goldbach's conjecture is wrong.")