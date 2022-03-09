s = str(input()).upper()
s_lst = list(set(s))
lst = []

for i in s_lst:
   lst.append(s.count(i))
if lst.count(max(lst)) >= 2:
    print("?")
else:
    print(s_lst[(lst.index(max(lst)))])
