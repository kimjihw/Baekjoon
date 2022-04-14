n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
    lst[i] = sorted(lst[i])
    print(lst[i][-3])