#15686 치킨 배달

import sys
from itertools import combinations
input=sys.stdin.readline

N, M= map(int,input().split())
array=[list(map(int,input().split())) for _ in range(N)]
home=[]
chicken=[]
for i in range(N):
    for j in range(N):
        if array[i][j]==1:
            home.append([i,j])
        if array[i][j]==2:
            chicken.append([i,j])
s=[]
for i in combinations(chicken,M):
    cnt=0
    for j in home:
        hcl=100
        for c in i:
            hcl= min(hcl, (abs(c[0]-j[0])+abs(c[1]-j[1])))
        cnt+= hcl
    s.append(cnt)


print(min(s))