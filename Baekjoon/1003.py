dp = [0]*41

def fibo(n):
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    for i in range(2, n+1):
        if dp[i] == 0:
            dp[i] = [dp[i-1][j]+dp[i-2][j] for j in range(2)]
    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    fibo(n)
    print(dp[n][0], dp[n][1])