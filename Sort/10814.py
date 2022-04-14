n = int(input())
total = []
for i in range(n):
    total.append([])
    total[i].append(int(input()))
    total[i].append(str(input()))

print(sorted(total, key=lambda x : x[0]))
