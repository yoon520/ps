import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 인접한 곳에 배추가 있는지 체크
def check(a, b):
    g[a][b] = 0

    if a > 0 and g[a-1][b]:
        check(a-1, b)

    if b > 0 and g[a][b-1]:
        check(a, b-1)

    if a < n-1 and g[a+1][b]:
        check(a+1, b)

    if b < m-1 and g[a][b+1]:
        check(a, b+1)

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().rstrip().split())
    g = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().rstrip().split())
        g[y][x] = 1

    cnt = 0

    # 완전탐색
    for i in range(n):
        for j in range(m):
            if g[i][j]:
                cnt += 1
                check(i, j)
    print(cnt)