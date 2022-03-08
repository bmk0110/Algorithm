# 1978 소수찾기

N = int(input())
array = list(map(int,input().split()))
answer=0
for i in array:
    error = 0
    if i!=1:
        for j in range(2,i):
            if i%j==0:
                error+=1
                break
        if error==0:
            answer+=1
print(answer)