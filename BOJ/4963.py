#4963 섬의 개수
from collections import deque
import sys

def BFS(a,b):
    queue = deque()
    queue.append((a,b))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<H and 0<=ny<W and maps[nx][ny]==1 and visited[nx][ny]==False:
                queue.append((nx,ny))
                visited[nx][ny]=True


dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, 1, -1, -1, 1, -1]

while True:
    W, H = map(int, input().split())
    maps=[]
    visited=[[False]*W for _ in range(H)]
    count = 0
    if (W, H) == (0,0):
        break
    for _ in range(H):
        maps.append(list(map(int, sys.stdin.readline().split())))
    for i in range(H):
        for j in range(W):
            if maps[i][j]==1 and visited[i][j]==False:
                BFS(i,j)
                count+=1

    print(count)


