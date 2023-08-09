import sys
# 재귀 깊이를 늘림 BOJ의 채점 서버에서 기본적으로 1000으로 지정되어 있음
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, start, visited):
    visited[start] = 1
    
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for i in range(m):
    u, v = map(int, input().rstrip().split())
    # 방향이 없는 그래프이기 때문에 양 방향으로 추가해줌
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    # 방문하지 않은 노드라면 새로운 연결 요소를 발견한 것으로 다시 dfs를 해줌
    if not visited[i]:
        cnt += 1
        dfs(graph, i, visited)

print(cnt)