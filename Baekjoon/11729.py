def hanoi(n, s, e, o):
    if n == 1:
        print(s, e)
        return
    
    hanoi(n-1, s, o, e)
    print(s, e)
    hanoi(n-1, o, e, s)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3, 2)