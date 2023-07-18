def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    if len(str(a)) > 9:
        print(str(a)[-9:])
    else:
        print(a)

a, b = 1, 1

n = int(input())
a_nums = list(map(int, input().split()))
for i in a_nums:
    a *= i

m = int(input())
b_nums = list(map(int, input().split()))
for i in b_nums:
    b *= i

gcd(a, b)