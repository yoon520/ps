import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    v[1] = 1
    q = deque([1])
    cnt = 0

    # 친구의 친구까지만 탐색
    for _ in range(2):
        for _ in range(len(q)):
            now = q.popleft()

            # 친구 카운트
            for i in f_li[now]:
                if not v[i]:
                    q.append(i)
                    v[i] = 1
                    cnt += 1
    return cnt

n = int(input())
m = int(input())

f_li = [[] for _ in range(n+1)]
v = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().rstrip().split())

    f_li[a].append(b)
    f_li[b].append(a)

print(bfs())