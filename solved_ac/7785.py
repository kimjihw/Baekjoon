import sys

n = int(sys.stdin.readline())
lst = []
stack = []
for i in range(n):
    lst.append(list(map(str, sys.stdin.readline().split())))

for i in lst:
    if i[1] == "enter":
        stack.append(i[0])
    if i[1] == "leave":
        stack.remove(i[0])

print(*sorted(stack, reverse=True), sep="\n")