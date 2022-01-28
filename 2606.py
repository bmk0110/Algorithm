#2606 바이러스
import sys

def dfs(a):
    global cnt
    for i in nodes[a]:
        if i not in final:
            cnt+=1
            final.append(i)
            dfs(i)


N=int(input())
M=int(input())
nodes=[[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

cnt = 0
final = [1]
if len(nodes[1]) ==0:
    print(0)
else:
    dfs(1)
    print(cnt)