s = str(input())
lst = []
for i in range(len(s)):
    lst.append(s[i::])
print(*sorted(lst), sep="\n")
