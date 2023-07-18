n = int(input())
nums = list(map(int, input().split()))
s = []
ans = [0]*n

for i in range(n):
    while s:
        if nums[i] > nums[s[-1]]:
            s.pop()
        else:
            ans[i] = s[-1]+1
            break
    s.append(i)

print(*ans)