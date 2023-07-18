n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

def sum_n(idx, total):
    global cnt
    if idx == n:  # 입력받은 정수 리스트를 전부 확인했다면
        return
    
    total += nums[idx]
    if total == s:
        cnt += 1

		# 현재 nums[idx]를 선택한 경우
    sum_n(idx+1, total)
		# 현재 nums[idx]를 선택하지 않은 경우
    sum_n(idx+1, total-nums[idx])

sum_n(0, 0)
print(cnt)