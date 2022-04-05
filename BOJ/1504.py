#1504 특정한 최단경로
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijk(start):
    q=[]
    heapq.heappush(q,(0,start))
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

N, E = map(int,input().split())
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)
for _ in range(E):
    a,b,c= map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
point1, point2 = map(int,input().split())
first=0
second=0

dijk(1)
first += distance[point1]
second += distance[point2]

distance = [INF]*(N+1)
dijk(point1)
first+=distance[point2]
second+=distance[N]

distance = [INF]*(N+1)
dijk(point2)
second+=distance[point1]
first+=distance[N]
final= min(first,second)
if final>=INF:
    print(-1)
else:
    print(final)
