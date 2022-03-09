from itertools import combinations

n, k = map(int,input().split())
lst = list(map(int, input().split()))
rst = list(combinations(lst, 3))
card = []
for i in rst:
    if sum(i) > k:
        continue
    else:
        card.append(sum(i))
print(max(card))
