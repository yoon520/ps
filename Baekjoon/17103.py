# N의 최대값까지 소수를 구해둔다.
m = 1000000
prime = [0, 0] + [1]*(m-1)

for i in range(2, 1001):
    if prime[i]:
        for j in range(i+i, m+1, i):
            prime[j] = 0

t = int(input())
for _ in range(t):
    cnt = 0
    n = int(input())

    # 두 소수의 합으로 되어있다면 카운트
    for i in range(2, n//2+1):
        if prime[i] and prime[n-i]:
            cnt += 1
    
    print(cnt)