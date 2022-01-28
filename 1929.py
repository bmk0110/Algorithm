#1929 소수 구하기
M, N = map(int,input().split())

if M==1:
    M+=1

for i in range(M,N+1):
    error=0
    #제곱근까지만 하면 됨
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            error=1
            break
    if error==0:
        print(i)