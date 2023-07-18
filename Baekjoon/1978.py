n = int(input())
arr = list(map(int, input().split()))

for i in arr:
    if i == 1:
        n -= 1
    else:
        for j in range(2,i):
            if i % j == 0:
                n -= 1
                break

print(n)