#1504 특정한 최단경로
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijk(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance = [INF] * (N + 1)

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
    return distance
N, E = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c= map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

point1, point2 = map(int,input().split())

first = dijk(1)[point1]+dijk(point1)[point2]+dijk(point2)[N]
second = dijk(1)[point2]+dijk(point2)[point1]+dijk(point1)[N]


if min(first,second)>=INF:
    print(-1)
else:
    print(min(first,second))
