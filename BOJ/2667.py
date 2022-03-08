#2667 단지번호붙이기

from collections import deque
def bfs(a,b):
    queue = deque()
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue.append((a,b))
    maps[a][b]=0
    visited[a][b]=True
    count = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            if 0<=nx<N and 0<=ny<N and maps[nx][ny]==1 and visited[nx][ny] == False:
                queue.append((nx,ny))
                visited[nx][ny]=True
                count+=1
    return count

N = int(input())
maps = []
visited=[[False]*N for _ in range(N)]
for _ in range(N):
    maps.append(list(map(int,input())))
final=[]
for i in range(N):
    for j in range(N):
        if maps[i][j]==1 and visited[i][j]==False:
            final.append(bfs(i,j))
final.sort()
print(len(final))
for i in range(len(final)):
    print(final[i])