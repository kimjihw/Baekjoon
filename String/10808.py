s = str(input())
lst = [0] * 26
rst = ""
for i in range(len(s)):
    lst[ord(s[i]) - 97] = s.count(s[i])
for i in lst:
    rst += str(i)
print(" ".join(rst))