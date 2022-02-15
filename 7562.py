#7562 나이트의 이동

from collections import deque

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    chess[a][b]=1
    dx = [2,1,-1,-2,-2,-1,1,2]
    dy = [1,2,2,1,-1,-2,-2,-1]
    while queue:
        x, y = queue.popleft()
        if x==fa and y==fb:
            print(chess[fa][fb]-1)
            break
        for i in range(8):

            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<l and 0<=ny<l and chess[nx][ny]==0 :
                queue.append((nx,ny))
                chess[nx][ny]= chess[x][y]+1
T=int(input())
for t in range(T):
    l = int(input())
    chess = [[0] *l for _ in range(l)]
    a, b = map(int,input().split())
    fa, fb = map(int,input().split())
    if a==fa and b== fb:
        print(0)
    else:
        bfs(a,b)
