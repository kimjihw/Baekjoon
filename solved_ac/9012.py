import sys

n = int(sys.stdin.readline())

for i in range(n):
    stack = []
    a = str(sys.stdin.readline())
    for j in a:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
