from collections import deque

# 이동 방향
move = [-1, 1, 2]
MAX_LENGTH = 100001

def bfs(start, end):
    global level, MAX_LENGTH
    q.append(start)
    v[start] = 1

    while q:
        # q 길이만큼 반복(같은 level 노드 탐색)
        for _ in range(len(q)):
            s = q.popleft()
            # 동생 위치와 같아지면 종료
            if s == end:
                return level
            for i in range(3):
                if i == 2:
                    now = s * move[i]
                else:
                    now = s + move[i]

                if 0 <= now <= MAX_LENGTH and v[now] == 0:
                    q.append(now)
                    v[now] = 1

        # 같은 level의 자식 노드 탐색이 끝났다면 level 증가(이동 횟수 증가)
        level += 1

n, k = map(int, input().split())
v = [0] * (MAX_LENGTH+1)
q = deque([])
level = 0

print(bfs(n, k))