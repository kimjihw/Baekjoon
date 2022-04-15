import sys

a, b = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

print(sorted(lst)[b-1])