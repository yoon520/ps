# 백트래킹
ans = []
def perm(n):
    if len(ans) == n:
        print(*ans)
        return
    for i in range(1, n+1):
        if i not in ans:
            ans.append(i)
            perm(n)
            ans.pop()

perm(int(input()))

# itertools.permutations 사용
import itertools
n = int(input())
p = itertools.permutations(range(1, n+1), n)
for i in p:
    print(*i)