import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
wv = [[0,0]]
knapsack = [[0 for _  in range(k+1)] for _ in range(n+1)]

for _ in range(n):
    wv.append(list(map(int, input().rstrip().split())))

for i in range(1, n+1):
    for j in range(1,k+1):
        if j < wv[i][0]:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(wv[i][1] + knapsack[i-1][j-wv[i][0]], knapsack[i-1][j])

print(knapsack[n][k])
