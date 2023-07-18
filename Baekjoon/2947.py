piece = list(map(int, input().split()))

while piece != [1, 2, 3, 4, 5]:
    for i in range(4):
        if piece[i] > piece[i+1]:
            piece[i], piece[i+1] = piece[i+1], piece[i]
            print(*piece)