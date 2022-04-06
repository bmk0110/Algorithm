import heapq
import sys
input= sys.stdin.readline
INF = int(1e9)
T = int(input())
def dijk(x,y):
    q = []
    heapq.heappush(q,(graph[0][0], (x,y)))
    distance[x][y]=graph[0][0]
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    while q:
        dist, (x, y) = heapq.heappop(q)
        if distance[x][y]<dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                d = dist + graph[nx][ny]
                if d<distance[nx][ny]:
                    distance[nx][ny]= d
                    heapq.heappush(q, (d, (nx,ny)))
for _ in range(T):
    N = int(input())
    graph=[]
    distance=[[INF]*N for _ in range(N)]
    for _ in range(N):
        graph.append(list(map(int,input().split())))
    dijk(0,0)
    print(distance[N-1][N-1])