#1753 최단경로

import heapq
import sys
input=sys.stdin.readline
INF = int(1e9)

def dijk(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            d= dist+i[0]
            if d<distance[i[1]]:
                distance[i[1]]=d
                heapq.heappush(q,(d,i[1]))

V, E = map(int,input().split())
start=int(input())
graph=[[]for _ in range(V+1)]
distance=[INF]*(V+1)
for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((w,v))

dijk(start)
for i in range(1,len(distance)):
    if distance[i]==INF:
        print('INF')
    else:
        print(distance[i])