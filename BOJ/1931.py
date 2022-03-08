#1931 회의실 배정
import sys
N = int(input())
array=[]
for _ in range(N):
    a,b= map(int,sys.stdin.readline().split())
    array.append([a,b])
array.sort(key = lambda x: (x[1],x[0]))
carray=[]
start = 0
# while start!=(len(array)-1):
last = 0
cnt = 0
for i in range(start,len(array)):
    if last<=array[i][0]:
        cnt+=1
        last=array[i][1]
# carray.append(cnt)
# start+=1
# print(max(carray))
print(cnt)