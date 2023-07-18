from collections import deque

n, m = map(int, input().split())
k = deque(map(int, input().split()))
nums = deque([i+1 for i in range(n)])
cnt = 0

while k:
    if k[0] == nums[0]:
        nums.popleft()
        k.popleft()
    else:
        i = nums.index(k[0])
        l = len(nums)
        if i <= l//2:
            nums.rotate(-i)
            cnt += i
        else:
            nums.rotate(l-i)
            cnt += l-i

print(cnt)