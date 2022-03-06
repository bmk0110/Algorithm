#2751 수정렬하기2
import sys
array=[]
n=int(input())
for _ in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()
for i in array:
    print(i)