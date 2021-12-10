s = str(input())
lst = [0] * 26
for i in range(len(s)):
    lst[ord(s[i]) - 97] = s.count(s[i])

for i in lst:
    print(i, end=" ")