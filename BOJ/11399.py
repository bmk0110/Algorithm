#11399 ATM
import sys
input= sys.stdin.readline
N = int(input())

array = list(map(int,input().split()))
array.sort()
final=0
mid=0
# print(array)
for i in array:
    mid+=i
    final+=mid
print(final)