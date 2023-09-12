from collections import deque

def bfs(s, g):
    v[s] = 1
    q = deque([s])

    while q:
        now = q.popleft()
        if now == g:
            # 스타트링크가 있는 층에 도착하면 함수 종료
            # 강호가 처음 있던 층을 1로 했기 때문에 버튼을 누른 횟수는 n-1
            return v[now]-1
        
        for next in (now+u, now-d):
            # 아래 위로 층이 있어서 버튼을 누를 수 있는 경우
            if 0 < next < f+1:
                if not v[next]:
                    q.append(next)
                    v[next] = v[now] + 1

    # while문을 돌고 q가 비어있다면 g에 도달하지 못함
    return "use the stairs"

f, s, g, u, d = map(int, input().split())
v = [0 for i in range(f+1)]

print(bfs(s, g))