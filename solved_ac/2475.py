lst = list(map(int, input().split()))
rst = []

for i in lst:
    rst.append(i**2)
print(sum(rst) % 10)