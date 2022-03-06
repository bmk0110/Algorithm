#2480 주사위 세개
import sys

a,b,c=map(int,sys.stdin.readline().split())
k=set([a,b,c])
array=[a,b,c]
array.sort()
prize=0
if len(k)==1:
    prize=10000+a*1000
elif len(k)==2:
    prize = 1000 + array[1] * 100
else:
    prize=max(k)*100
print(prize)