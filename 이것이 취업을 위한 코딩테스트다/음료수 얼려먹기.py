import sys
from collections import deque
# input=sys.stdin.readline
dx= [1,-1,0,0]
dy= [0,0,1,-1]
def bfs(a,b):
    queue = deque()
    visited[a][b] = 1
    queue.append((a,b))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny= y+dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0 and array[nx][ny]==0:
                queue.append((nx,ny))
                visited[nx][ny]=1



N, M =map(int,input().split())
array=[list(map(int,input())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
cnt=0
for i in range(N):
    for j in range(M):
        if array[i][j]==0 and visited[i][j] ==0:
            bfs(i,j)
            cnt+=1
print(cnt)