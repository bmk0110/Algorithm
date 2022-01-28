#덩치

N = int(input())
peoples = []
for i in range(N):
    a = list(map(int,input().split()))
    peoples.append(a)

peoples.sort(reverse=True)
print(peoples)

