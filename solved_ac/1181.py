n = int(input())
lst = []
for i in range(n):
    lst.append(str(input()))

lst = list(set(lst))
lst.sort(key= lambda x : x)
lst.sort(key= lambda x : len(x))

for i in lst:
    print(i)