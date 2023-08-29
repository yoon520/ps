from collections import deque

def bfs(x, y):
    mx = [0, 1, 0, -1]
    my = [1, 0, -1, 0]

    q = deque([(x, y)])
    v[x][y] = 1

    while q:
        now = q.popleft()

        for i in range(4):
            nx = now[0] + mx[i]
            ny = now[1] + my[i]

            if 0<=nx<n and 0<=ny<n:
                # 상하좌우 노드 중 색상이 같은 노드 방문
                if g[now[0]][now[1]] == g[nx][ny] and v[nx][ny] == 0:
                    q.append((nx, ny))
                    v[nx][ny] = 1

n = int(input())
g = []
v = [[0 for _ in range(n)] for _ in range(n)]
# 색약이 아닌 사람
noncolorb = 0
# 색약인 사람
colorb = 0

for _ in range(n):
    g.append(list(input()))

# 적록색약이 아닌 사람이 보는 구역 구하기
for i in range(n):
    for j in range(n):
        if v[i][j] == 0:
            noncolorb += 1
            bfs(i, j)

# G를 R로 치환해서 R과 B만 남김
for i in range(n):
    for j in range(n):
        if g[i][j] == 'G':
            g[i][j] = 'R'

v = [[0 for _ in range(n)] for _ in range(n)]

# 적록색약인 사람이 보는 구역 구하기
for i in range(n):
    for j in range(n):
        if v[i][j] == 0:
            colorb += 1
            bfs(i, j)
            
print(noncolorb, colorb)