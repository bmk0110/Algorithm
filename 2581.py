#2581 소수

M = int(input())
N = int(input())
array=[]
for i in range(M,N+1):
    error=0
    if i !=1:
        for j in range(2,i):
            if i % j ==0:
                error = 1
                break
        if error ==0 :
            array.append(i)
if len(array)==0:
    print(-1)
else:
    print(sum(array))
    print(min(array))