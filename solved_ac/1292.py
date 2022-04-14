lst = []
a, b = map(int,input().split())
for i in range(1, 1000):
    for j in range(i):
        lst.append(i)
print(sum(lst[a -1 : b]))