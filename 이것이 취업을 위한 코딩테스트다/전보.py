import heapq
import sys
input= sys.stdin.readline
INF = int(1e9)

n, m, c = map(int,input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int,input().split())
    graph[x].append((z,y))

def dijk(start):
    q=[]
    heapq.heappush(q,(0, start))
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            d= dist+i[0]
            if d<distance[i[1]]:
                distance[i[1]]=d
                heapq.heappush(q,(d,i[1]))
dijk(c)
cnt=-1
maxd=0
for d in distance:
    if d!=INF:
        cnt+=1
        if maxd<d:
            maxd=d

# print(graph)
# print(distance)
print(cnt,maxd)