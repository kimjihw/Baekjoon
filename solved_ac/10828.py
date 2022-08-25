import sys

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    s = sys.stdin.readline().split()
    for j in s:
        if j == "pop":
            if not stack:
                print(-1)
            else:
                print(stack[-1])
                stack.pop()
        elif j == "top":
            if not stack:
                print(-1)
            else:
                print(stack[-1])
        elif j.isdecimal():
            stack.append(j)
        elif j == "size":
            print(len(stack))
        elif j == "empty":
            if stack:
                print(0)
            else:
                print(1)