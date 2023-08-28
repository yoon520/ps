from collections import deque

def bfs():
    mx = [0, 1, 0, -1]
    my = [1, 0, -1, 0]

    q = deque([(0,0)])

    while q:
        now = q.popleft()
        if now == (n-1, m-1):
            return g[n-1][m-1]
        for i in range(4):
            nx = now[0] + mx[i]
            ny = now[1] + my[i]

            if 0<=nx<n and 0<=ny<m:
                if g[nx][ny]==1 and (nx,ny) != (0,0):
                    q.append((nx,ny))
                    g[nx][ny] = g[now[0]][now[1]] + 1

n, m = map(int, input().split())
g = []

for _ in range(n):
    g.append(list(map(int, input())))

print(bfs())