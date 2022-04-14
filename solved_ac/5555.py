s = str(input())
n = int(input())
cnt = 0
lst = []

for i in range(n):
    lst.append(str(input()) * 2)

for i in lst:
    if(s in i):
        cnt = cnt + 1

print(cnt)
