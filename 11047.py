#11047 동전0

N,K = map(int,input().split())
array=[]
cnt=0
for _ in range(N):
    array.append(int(input()))
for i in range(N-1,-1, -1):
    if K>=array[i]:
        while K>=array[i]:
            K-=array[i]
            cnt+=1
print(cnt)