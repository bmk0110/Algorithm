#7569 토마토
from collections import deque
import sys
input=sys.stdin.readline
dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
def bfs():


    while queue:
        x , y, z = queue.popleft()
        for a in range(6):
            nx= x+dx[a]
            ny=y+dy[a]
            nz=z+dz[a]
            if 0 <= nx < H and 0 <= ny < N and 0<=nz< M and box[nx][ny][nz] == 0:
                box[nx][ny][nz] = box[x][y][z] + 1
                queue.append((nx, ny, nz))


M, N, H = map(int, input().split())
box=[]
cnt=0
queue = deque()
for _ in range(H):
    array = []
    for _ in range(N):
        array.append(list(map(int,input().split())))
    box.append(array)
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k]==1:
                queue.append((i, j, k))
# print(queue)
bfs()
for i in box:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        if cnt < max(j):
            cnt = max(j)
print(cnt-1)