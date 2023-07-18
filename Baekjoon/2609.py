n, m = map(int, input().split())

# 재귀
def gcd(n, m):
    if n%m == 0:
        return m
    return gcd(m, n%m)

# 반복문
def gcd(n, m):
    while m > 0:
        n, m = m, n%m
    return n

num = gcd(n, m)
print(num)
print(n*m//num)