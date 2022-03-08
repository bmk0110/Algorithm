#1012 유기농 배추
import sys
from collections import deque

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        visited[x][y]=True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and maps[nx][ny]==1 and visited[nx][ny]==False:
                visited[nx][ny]=True
                queue.append((nx,ny))

T= int(input())
for _ in range(T):
    M, N, K = map(int,input().split())
    maps=[[0]*M for _ in range(N)]
    visited=[[False]*M for _ in range(N)]
    cnt=0
    for _ in range(K):
        a,b = map(int, sys.stdin.readline().split())
        maps[b][a] = 1
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(N):
        for j in range(M):
            if maps[i][j]==1 and visited[i][j]==False:
                bfs(i,j)
                cnt+=1
    print(cnt)

