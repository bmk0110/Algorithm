#15650 N과 M (2)

# def dfs(cnt):
#     if cnt==M:
#         print(*fp)
#     for i in range(N):
#         if check[i]==True:
#             continue
#         check[i]=True
#         fp.append(arr[i])
#         dfs(cnt+1)
#         fp.pop()
#         for j in range(i+1,N):
#             check[j]=False
#
#
# N,M=map(int,input().split())
# check=[False]*N
# arr=[i+1 for i in range(N)]
# fp=[]
#
#
# dfs(0)

from itertools import combinations

N, M = map(int, input().split())
arr = [i for i in range(1,N+1)]
for e in list(combinations(arr, M)):
    print(*e)