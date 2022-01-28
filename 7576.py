#7576 토마토
from collections import deque
import sys

def bfs():

    while queue:
        x,y= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and array[nx][ny]==0:
                array[nx][ny]= array[x][y]+1
                queue.append((nx,ny))
dx=[-1,1,0,0]
dy=[0,0,-1,1]

M, N = map(int, input().split())
array=[]
count=0
queue = deque()
First=[]
for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))

for i in array:
    for j in i:
        if j ==0:
            First.append(0)
if len(First)==0:
    print(0)
else:

    for i in range(N):
        for j in range(M):
            if array[i][j]==1:
                queue.append((i,j))
    bfs()
    for i in array:
        for j in i:
            if j ==0:
                print(-1)
                exit(0)
        if count<max(i):
            count = max(i)
    print(count-1)