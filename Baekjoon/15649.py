# 백트래킹
n, m = map(int, input().split())
ans = [] # 후보

def back():
    if len(ans) == m: # 후보가 정답 길이가 됐다면 출력
        print(" ".join(map(str, ans)))
        return
    for i in range(1, n+1):
        if i not in ans: # 후보에 i가 없으면 추가
            ans.append(i)
            back()  # 재귀
            ans.pop()  # retrun 후 실행 코드

back()

# itertools 모듈의 permutations() 사용
import itertools

n, m = map(int, input().split())
p = itertools.permutations(range(1,n+1), m)
for i in p:
    print(" ".join(map(str, i)))