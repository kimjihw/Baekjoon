import sys
from collections import Counter

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
rst = [0] * m

count = Counter(lst)
print(count)
for i in range(m):
    if card[i] in count:
        print(count[card[i]], end =" ")
    else:
        print(0, end=" ")