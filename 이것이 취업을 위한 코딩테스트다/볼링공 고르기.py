import sys
input=sys.stdin.readline
N, M = map(int,input().split())
array= list(map(int,input().split()))
cnt=0
for i in range(N-1):
    for j in range(i,N):
        if array[i]!=array[j]:
            cnt+=1
print(cnt)


