s = str(input())
find = str(input())
modify = ""

for i in s:
    if i.isalpha():
        modify += i
    else:
        continue
if find in modify:
    print(1)
else:
    print(0)