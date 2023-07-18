def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

n = int(input())
nums = sorted([int(input()) for _ in range(n)])
sub = [nums[i]-nums[i-1] for i in range(1,n)]

g = sub[0]
for i in range(1,n-1):
    g = gcd(g, sub[i])

result = set()
for i in range(2, int(g**0.5)+1):
    if g % i == 0:
        result.add(i)
        result.add(g // i)
result.add(g)

print(*sorted(list(result)))