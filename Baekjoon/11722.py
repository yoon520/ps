n = int(input())
dp = [0] * n
a = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if a[i] < a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))