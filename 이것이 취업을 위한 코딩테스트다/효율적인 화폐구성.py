import sys
input = sys.stdin.readline
N,M = map(int,input().split())
arr=[int(input()) for _ in range(N)]
arr.sort()
d=[10001]*(M+1)
d[0]=0
for i in arr:
    if i <=M:
        for j in range(i, M+1):
            if d[j-i]!=10001:
                d[j]=min(d[j],d[j-i]+1)
if d[M]==10001:
    print(-1)
else:
    print(d[M])
