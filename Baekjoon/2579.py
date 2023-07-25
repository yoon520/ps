n = int(input())
dp = [[0,0] for _ in range(n+1)]

for i in range(1, n+1):
    step = int(input())
    
    if i == 1:
        dp[i][0] = step
        dp[i][1] = step
    else:
        dp[i][0] = dp[i-1][1] + step
        dp[i][1] = max(dp[i-2]) + step

print(max(dp[n]))