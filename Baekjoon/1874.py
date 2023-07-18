import sys
input = sys.stdin.readline

n = int(input())
s, ans = [], []
cnt = 1

for i in range(n):
    k = int(input())
    
    while cnt <= k:
            s.append(cnt)
            ans.append("+")
            cnt += 1
    if s[-1] == k:
        s.pop()
        ans.append("-")

if not s:
    print(*ans, sep="\n")
else:
    print("NO")