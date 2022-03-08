#2573 빙산
from collections import deque
import sys

dx= [-1,1,0,0]
dy=[0,0,-1,1]

def bfs(a,b):
    queue=deque()
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        visited[x][y]=True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and array[nx][ny]!=0 and visited[nx][ny]==False:
                queue.append((nx,ny))
                visited[nx][ny]=True
            elif array[nx][ny]==0:
                minus[x][y]+=1

N, M = map(int, input().split())
array=[]
for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))
count = 0

answer = 0
while count<2:
    count = 0
    visited = [[False] * M for _ in range(N)]
    minus = [[0]*M for _ in range(N)]
    if max(map(max, array)) == 0:
        break
    for i in range(1,N-1):
        for j in range(1,M-1):
            if array[i][j]!=0 and visited[i][j]==False:
                bfs(i,j)
                count+=1
    for i in range(1, N-1):
        for j in range(1,M-1):
            if array[i][j]!=0:
                array[i][j]-=minus[i][j]
                if array[i][j]<0:
                    array[i][j]=0
    answer += 1

if count >= 2:
    print(answer-1)
else:
    print(0)