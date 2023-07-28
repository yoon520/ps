n = int(input())
dp = [0] * (n+1)
cup = [0] * (n+1)

for i in range(1, n+1):
    cup[i] = int(input())

    if i < 3:
        dp[i] = dp[i-1] + cup[i]
    else:
        # i번째 와인을 마시지 않고 i-1까지 마시는 경우도 계산해야 한다.
        dp[i] = max(dp[i-2]+cup[i], dp[i-3]+cup[i-1]+cup[i], dp[i-1])

print(dp[n])
