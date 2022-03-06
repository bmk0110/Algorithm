#10989 수 정렬하기 3

import sys
array=[0]*10000
n=int(input())
for _ in range(n):
    array[(int(sys.stdin.readline()))-1]+=1

for i in range(10000):
    if array[i] !=0:
        for j in range(array[i]):
            print(i+1)