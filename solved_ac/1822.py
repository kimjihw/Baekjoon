a, b = map(int, input().split())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

a_set = set(a_lst)
b_set = set(b_lst)
if len(list(a_set - b_set)) == 0:
    print(0)
else:
    print(len(list(a_set-b_set)))
    print(*sorted(list(a_set - b_set)), end=" ")