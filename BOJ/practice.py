# from collections import deque
# import sys
# N, M = map(int, input().split())
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, input())))
# queue= deque()
# queue.append((0,0))
# dx=[-1,1,0,0]
# dy=[0,0,-1,1]
# while queue:
#     x,y = queue.popleft()
#     for i in range(4):
#         nx = x+dx[i]
#         ny= y+dy[i]
#         if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1:
#             graph[nx][ny]= graph[x][y]+1
#             queue.append((nx,ny))
# print(graph[N-1][M-1])

# import sys
# input=sys.stdin.readline
# N=int(input())
# for _ in range(N):
#     array= list(map(int, input().split()))
#     score=sum(array[1:])/array[0]
#     count=0
#     for i in range(1,len(array)):
#         if array[i]>score:
#             count+=1
#     print(f'{(count/array[0])*100:0.3f}%')

# def infn(n):
#     if n<10000:
#         print(n+n//1000+n//100+n//10+n%10)
#         infn(n+n//1000+n//100+n//10+n%10)

# abc='abcdefghijklmnopqrstuvwxyz'
#
# T= int(input())
# count=0
# for t in range(T):
#     array = []
#     n=input()
#     real=True
#     for i in range(len(n)):
#         if n[i] not in array:
#             array.append(n[i])
#         else:
#             if n[i-1] != n[i]:
#                 real=False
#                 # print(n)
#     if real==True:
#         count+=1
#         # print(n)
# print(count)

import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 8)
print(heap)