from collections import deque

def bfs(p, x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    v[x][y] = 1
    q = deque([(x, y)])

    while q:
        now = q.popleft()

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if not v[nx][ny] and m[nx][ny]>p:
                    v[nx][ny]=1
                    q.append((nx, ny))

n = int(input())
m = []
max_height, max_cnt = 0, 0

for i in range(n):
    m.append(list(map(int, input().split())))
    max_height = max(max_height, max(m[i]))

for i in range(max_height):
    cnt = 0
    v = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for k in range(n):
            if not v[j][k] and m[j][k]>i:
                cnt += 1
                bfs(i, j, k)
    max_cnt = max(max_cnt, cnt)

print(max_cnt)