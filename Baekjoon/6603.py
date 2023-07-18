# 백트래킹
import sys

while True:
    s = list(map(int, sys.stdin.readline().split()))
    k = s.pop(0)
    if k == 0:
        break

    ans = []

    def comb(level):
        if len(ans)==6:
            print(" ".join(map(str, ans)))
            return
        for i in range(level, k):
            if s[i] not in ans:
                ans.append(s[i])
                comb(i+1)
                ans.pop()

    comb(0)
    print("")

# itertools 모듈의 combinations 함수
import sys
import itertools

while True:
    s = list(map(int, sys.stdin.readline().split()))
    k = s.pop(0)
    if k == 0:
        break

    c = itertools.combinations(s, 6)
    for i in c:
        print(*i)

    print("")