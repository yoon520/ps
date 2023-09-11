from collections import deque
def bfs(i, j, union_num):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    v[i][j] = union_num
    q = deque([(i, j)])

    while q:
        now = q.popleft()
        # union_num번째 연합의 연합의 인구수, 국가 개수 더하기
        sum[union_num-1][0] += a[now[0]][now[1]]
        sum[union_num-1][1] += 1

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if v[nx][ny] == 0:
                    # 인접 국가와 인구수 차이가 l 이상 r 이하인 경우
                    if l<=abs(a[now[0]][now[1]]-a[nx][ny])<=r:
                        # union_num번째 연합에 추가
                        v[nx][ny] = union_num
                        q.append((nx, ny))


n, l, r = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
# 이동 날짜
cnt = 0

while True:
    v = [[0 for _ in range(n)] for _ in range(n)]
    sum = []
    # 연합 개수
    union_num = 0
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                union_num += 1
                # 연합의 인구수, 연합의 국가 개수 초기화
                sum.append([0,0])
                bfs(i, j, union_num)

    # 연합 개수가 전체 칸 수와 같으면 더이상 인구이동이 일어나지 않으므로 종료
    if union_num == n*n:
        print(cnt)
        break

    cnt += 1
    for i in range(n):
        for j in range(n):
			# 인구 이동(소속된 연합의 인구수/국가)
            a[i][j] = sum[v[i][j]-1][0]//sum[v[i][j]-1][1]