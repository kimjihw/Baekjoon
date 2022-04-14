n = int(input())
lst = list(map(int, input().split()))

lst = sorted(lst)
if(len(lst) == 1):
    print(int(lst[0]) * int(lst[0]))
else:
    print(int(lst[0]) * int(lst[len(lst) -1]))
