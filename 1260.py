#1260 DFS와 BFS
from collections import deque
import sys

def dfs(n):
    print(n, end=' ')
    visited[n] = True
    for i in array[n]:
        if not visited[i]:
            dfs(i)
def bfs(n):
    visited[n]=True
    queue = deque([n])
    while queue:
        V = queue.popleft()
        print(V, end=' ')
        for i in array[V]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



N, M, V = map(int, input().split())
array=[[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    array[a].append(b)
    array[b].append(a)
for i in range(1,N+1):
    array[i].sort()
dfs(V)
visited = [False] * (N + 1)
print()
bfs(V)