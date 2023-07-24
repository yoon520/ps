n = int(input())
dp = [[0]*10 for _ in range(n)]
for i in range(1,10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(10):
        # 길이가 i일 때 마지막 숫자가 0일 경우
        if j == 0:
            dp[i][j] = dp[i-1][1]
        # 1~8일 경우
        elif 0 < j < 9:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        # 9일 경우
        else:
            dp[i][j] = dp[i-1][8]

print(sum(dp[n-1])%1000000000)