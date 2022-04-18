n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
print(*sorted(lst, reverse=True), sep="\n")