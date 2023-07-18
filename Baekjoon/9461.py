p = [0, 1, 1]

for i in range(3,101):
    p.append(p[i-2]+p[i-3])


n = int(input())
for _ in range(n):
    print(p[int(input())])