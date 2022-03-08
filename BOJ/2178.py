# from collections import deque
# import sys
#
#
#
#
# N, M = map(int, input().split())
# graph = []
#
# for _ in range(N):
#   graph.append(list(map(int, input())))
# dx=[-1, 1, 0, 0]
# dy= [0,0,-1,1]
# queue = deque()
# queue.append((0,0))
# while queue:
#     x, y = queue.popleft()
#
#     # 현재 위치에서 4가지 방향으로 위치 확인
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         # 위치가 벗어나면 안되기 때문에 조건 추가
#         if nx >= 0 and nx < N and ny >= 0 and ny < M and graph[nx][ny]==1:
#                 queue.append((nx,ny))
#                 graph[nx][ny] = graph[x][y]+1
#
# print(graph[N-1][M-1])

from collections import deque

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1 :
                graph[nx][ny]= graph[x][y]+1
                queue.append((nx,ny))

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input())))
bfs(0,0)
print(graph[N-1][M-1])