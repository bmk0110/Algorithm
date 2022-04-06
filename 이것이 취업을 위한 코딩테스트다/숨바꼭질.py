import heapq
import sys
input= sys.stdin.readline
INF = int(1e9)

def dijk(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist, now= heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            d = dist+i[0]
            if d < distance[i[1]]:
                distance[i[1]]=d
                heapq.heappush(q,(d,i[1]))


N,M=map(int,input().split())
graph = [[] for _ in range(N+1)]
distance=[INF]*(N+1)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append((1,b))
    graph[b].append((1,a))
dijk(1)

arr=[]
distance[0]=0
for i in range( 1,N+1):
    if distance[i] == max(distance):
        arr.append(i)
print(arr[0], distance[arr[0]], len(arr))