from collections import deque

k = int(input())

for _ in range(k):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    order = deque([i for i in range(n)])
    cnt = 0
    while q:
        # 제일 첫번째 요소가 가장 큰 수라면 pop
        if q[0] == max(q):
            cnt += 1
            # m번째 숫자라면 몇 번째로 인쇄됐는지 출력하고 멈춤
            if order[0] == m:
                print(cnt)
                break
            q.popleft()
            order.popleft()
        else:
            q.rotate(-1)
            order.rotate(-1)

