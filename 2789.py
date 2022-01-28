#블랙잭

N, M = map(int,input().split())
cards = list(map(int,input().split()))
sum=[]

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if M-(cards[i]+cards[j]+cards[k])>=0:
                sum.append(cards[i]+cards[j]+cards[k])

sum.sort(reverse=True)

print(sum[0])