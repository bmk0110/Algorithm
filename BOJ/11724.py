#11724 연결 요소의 개수
import sys
N,M = map(int,input().split())
array=[[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    array[a].append(b)
    array[b].append(a)
for i in range(N+1):
    array[i].sort()

