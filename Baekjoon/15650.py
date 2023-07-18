# 백트래킹
n, m = map(int, input().split())
ans = []

def comb(level):
    if len(ans)==m:
        print(' '.join(map(str, ans)))
        return
    for i in range(level, n+1):
        if i not in ans:
            ans.append(i)
            comb(i+1)
            ans.pop()

comb(1)

#combinations() 함수 사용
import itertools

n, m = map(int, input().split())
c = itertools.combinations(range(1,n+1), m)
for i in c:
    print(" ".join(map(str, i)))