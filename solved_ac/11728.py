a, b =map(int, input().split())
a_lst = list(map(int,input().split()))
b_lst = list(map(int, input().split()))

print(*sorted(a_lst + b_lst), end=" ")