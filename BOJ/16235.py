#16235 나무재테크
N,M,K= map(int,input().split())
A=[list(map(int,input().split()))for _ in range(N)]
T=[[[] for _ in range(N)] for _ in range(N)]
Vita = [[5 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x,y,z=map(int,input().split())
    T[x-1][y-1].append(z)

for _ in range(K):
    for i in range(N):
        for j in range(N):
            if len(T[i][j])>0:
                T[i][j].sort()
                a=0
                while a <(len(T[i][j])):
                    if T[i][j][a]<=Vita[i][j]:
                        Vita[i][j] -= T[i][j][a]
                        T[i][j][a]+=1
                        a+=1
                    else:
                        Die=T[i][j][a:]
                        T[i][j]=T[i][j][:a]
                        for y in range(len(Die)):
                            Vita[i][j] += Die[y] // 2
                        break

    dr=[-1,-1,-1,0,0,1,1,1]
    dc=[-1,0,1,-1,1,-1,0,1]
    for i in range(N):
        for j in range(N):
            cnt = 0
            if T[i][j]:
                for a in range(len(T[i][j])):
                    if T[i][j][a] % 5 == 0:
                        cnt += 1
            if cnt > 0:
                for b in range(8):
                    ni = i + dr[b]
                    nj = j + dc[b]
                    if 0 <= ni < N and 0 <= nj < N:
                        for _ in range(cnt):
                            T[ni][nj].append(1)

    for i in range(N):
        for j in range(N):
            Vita[i][j]+=A[i][j]

cnt=0
for i in range(N):
    for j in range(N):
        cnt+=len(T[i][j])
print(cnt)