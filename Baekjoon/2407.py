npm, r = 1, 1
n, m = map(int, input().split())

for i in range(n, n-m, -1):
    npm *= i
for i in range(1,m+1):
    r *= i
print(npm//r)
