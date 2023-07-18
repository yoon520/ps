n = int(input())
s = input()
nums = [0]*n

for i in range(n):
    nums[i] = int(input())

# 후위표기식 계산
stack = []

for i in s:
    if 'A' <= i <= 'Z':
        stack.append(nums[ord(i)-ord('A')])
    else:
        op2 = stack.pop()
        op1 = stack.pop()

        if i == "*":
            stack.append(op1*op2)
        elif i == "/":
            stack.append(op1/op2)
        elif i == "+":
            stack.append(op1+op2)
        elif i == "-":
            stack.append(op1-op2)

print(f"{stack[0]:.2f}")