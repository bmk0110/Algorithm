import sys
input=sys.stdin.readline

N, M = map(int,input().split())
A, B, d = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(M)]
visited= [[0]*N for _ in range(M)]
visited[A][B] = 1
dx=[-1,0,1,0]
dy=[0,1,0,-1]
cnt=1
#방향 돌린 횟수
turn=0
while True:
    #좌회전
    d-=1
    if d==-1:
        d=3
    nx = A + dx[d]
    ny = B + dy[d]

    if visited[nx][ny]==0 and array[nx][ny]==0:
        visited[nx][ny]=1
        A = nx
        B = ny
        cnt+=1
        turn=0
    else:
        turn+=1

    if turn ==4 :
        nx= A - dx[d]
        ny = B - dy[d]
        if array[nx][ny]==1:
            break
        else:
            A = nx
            B= ny
        turn=0
print(cnt)