#13305 주유소
# import sys
# input = sys.stdin.readline()
N = int(input())
distance = list(map(int,input().split()))
city = list(map(int,input().split()))
minv=city[0]
money= minv*distance[0]
for i in range(1,len(city)-1):
    if city[i]<minv:
        minv=city[i]
    money+= minv*distance[i]

print(money)
