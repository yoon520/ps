import sys
input = sys.stdin.readline

n = int(input())
t = {}

for i in range(n):
    root, left, right = input().rstrip().split()
    t[root] = [left, right]
k = list(t.keys())

# 전위 순회 (루트 -> 왼쪽 자식 -> 오른쪽 자식)
def preorder(root):
    if root != '.':
        print(root, end="")
        preorder(t[root][0])
        preorder(t[root][1])

# 중위 순회 (왼쪽 자식 -> 루트 -> 오른쪽 자식)
def inorder(root):
    if root != '.':
        inorder(t[root][0])
        print(root, end="")
        inorder(t[root][1])

# 후위 순회 (왼쪽 자식 -> 오른쪽 자식 -> 루트)
def postorder(root):
    if root != '.':
        postorder(t[root][0])
        postorder(t[root][1])
        print(root, end="")

preorder(k[0])
print()
inorder(k[0])
print()
postorder(k[0])
