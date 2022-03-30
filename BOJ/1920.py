#1920 수찾기
import sys
input = sys.stdin.readline
N = int(input())
A=list(map(int,input().split()))
k=[0]*2**31
for i in A:
    k[i]=1
M=int(input())
B=list(map(int,input().split()))
for i in B:
    print(k[i])