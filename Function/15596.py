def solve(a):
    print(sum(a))
    return sum(a)

n = int(input())
a = list(map(int, input().split()))
solve(a)