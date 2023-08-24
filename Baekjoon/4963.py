import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    mx = [-1, 0 , 1]
    my = [-1, 0 , 1]

    m[x][y] = 0

    for i in mx:
        for j in my:
            nx = x + i
            ny = y + j

            if 0<=nx<h and 0<=ny<w:
                if m[nx][ny]:
                    dfs(nx, ny)

while True:
    cnt = 0
    w, h = map(int, input().rstrip().split())
    if (w, h) == (0, 0):
        break
    
    m = []
    for _ in range(h):
        m.append(list(map(int, input().rstrip().split())))

    for i in range(h):
        for j in range(w):
            if m[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)