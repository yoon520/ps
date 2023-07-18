n = int(input())
nums = list(map(int, input().split()))
s = []
ans = [-1]*n

for i in range(n):
    while s and nums[s[-1]] < nums[i]:
        ans[s.pop()] = nums[i]
    s.append(i)

print(*ans)