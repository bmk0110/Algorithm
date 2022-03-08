#2292 벌집

N = int(input())
bee=1
cnt=1
while bee<N:
    bee+= 6*cnt
    cnt+=1
print(cnt)