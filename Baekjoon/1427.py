# sort() 함수 사용
n = list(input())
n.sort(reverse=True)
print(''.join(n))

# 퀵 정렬
def quick(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]
    left, right, equal = [], [], []

    for i in arr:
        if pivot < i:
            left.append(i)
        elif pivot > i:
            right.append(i)
        else:
            equal.append(i)

    return quick(left) + equal + quick(right)

n = list(input())
print(''.join(quick(n)))