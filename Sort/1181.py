# n = int(input())
# lst = []
# for i in range(n):
#     s = str(input())
#     lst.append(s)
# lst = list(set(lst))
# lst = sorted(lst, key = len)
# print(lst)

from collections import deque

def bfs(graph, root):
    visit = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visit:
            visit.append(n)
            queue += graph[n] - set(visit)
        print(visit, queue)
    return visit

graph = {1: set([3,4]),
         2 : set([3,4,5]),
         3: set([1,5]),
         4: set([1]),
         5: set([2, 6]),
         6: set([3, 5])}
root = 1
print(bfs(graph, root))