import sys
input = sys.stdin.readline

def dfs(x, y):
    mx = [1, -1, 0, 0]
    my = [0, 0, 1, -1]

    g[x][y] = 0
    # 현재 탐색 중인 단지의 집 수 추가
    house[-1] += 1

    for i in range(4):
        nx = x + mx[i]
        ny = y + my[i]

        if( 0<=nx<n) and (0<=ny<n):
            if g[nx][ny] == 1:
                dfs(nx, ny)

n = int(input())
g = []
# 단지 수
cnt = 0
# 단지별 집 수
house = []

for _ in range(n):
    g.append(list(map(int, input().rstrip())))

for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            cnt += 1
            # 새로운 단지를 확인하면 해당 단지의 집 수를 0으로 초기화해서 추가해준다.
            house.append(0)
            dfs(i, j)

print(cnt)
house.sort()
print(*house, sep='\n')