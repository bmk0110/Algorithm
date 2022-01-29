#1037 약수
import sys

N = int(input())

array = list(map(int,sys.stdin.readline().split()))

array.append(1)
array.sort()
if len(array)==2:
    print(array[1]**2)
elif len(array)%2==1:
    print(array[N//2]*array[N//2+1])
elif len(array)%2==0:
    print(array[N//2+1]**2)