def gcd(a, b):
    while a % b > 0:
        a, b = b, a % b
    return b

n, x = map(int, input().split())
a = list(map(int, input().split()))
a.append(x)
a.sort()

D = a[1]-a[0]
for i in range(2, n+1):
    D = gcd(D, a[i]-a[i-1])
print(D)