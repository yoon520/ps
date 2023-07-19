from math import comb

n = int(input())

total = 0
for i in range(n//2+1):
    single = n-i*2
    print(comb(single+i, i))
    total += comb(single+i, i)

print(total%10007)