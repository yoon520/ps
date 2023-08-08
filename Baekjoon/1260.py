from collections import deque

# 깊이 우선 탐색
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 넓이 우선 탐색
def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

n, m, v = map(int, input().split())
graph =[[] for _ in range(n+1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
	# 인접 노드 번호 저장
    graph[v1].append(v2)
    graph[v2].append(v1)
# 인접 노드 오름차순으로 정렬
for i in graph:
    i.sort()

visited = [False] * (n+1)
dfs(graph, v, visited)

print()

visited = [False] * (n+1)
bfs(graph, v, visited)