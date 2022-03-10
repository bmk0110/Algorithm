from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(a,b):
    global cnt
    queue=deque()
    queue.append((a,b))
    while queue:
        x,y= queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and miro[nx][ny]==1:
                queue.append((nx,ny))
                miro[nx][ny]= miro[x][y]+1

N, M = map(int,input().split())
miro = [list(map(int,input())) for _ in range(N)]
cnt=1
bfs(0,0)
print(miro[N-1][M-1])