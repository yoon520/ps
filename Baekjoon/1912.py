n = int(input())
arr = list(map(int, input().split()))
dp = [arr[0]]

for i in range(1, n):
    # 합이 커지려면 양수가 더해져야 하기 때문에
    if dp[-1] > 0:
        dp.append(dp[-1]+arr[i])
    else:
        dp.append(arr[i])
        
print(max(dp))