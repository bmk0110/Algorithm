#1931 회의실 배정
import sys
N = int(input())
array=[]
for _ in range(N):
    a,b= map(int,sys.stdin.readline().split())
    array.append([a,b])
array.sort()
carray=[]
s=0
while True:
    array[s]