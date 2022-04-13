lst = []
srt = ""
for i in range(8):
    lst.append(int(input()))
s_lst = sorted(lst)
rst = s_lst[3:8]
hap = sum(rst)
print(hap)
index = []
for i in rst:
    index.append(lst.index(i) + 1)
index = sorted(index)
for i in index:
    srt = srt + str(i)
print(" ".join(srt))
