#7568 덩치

N = int(input())
peoples = []
for i in range(N):
    a = list(map(int,input().split()))
    peoples.append(a)
cnt=0
rank=[]
for i in range(len(peoples)):
    cnt=1
    for j in range(len(peoples)):
        if peoples[i][0]<peoples[j][0] and peoples[i][1]<peoples[j][1]:
            cnt+=1
    rank.append(cnt)

for i in range(len(rank)):
    print(rank[i],end=' ')