#12865 평범한 배낭
import sys
N, K = map(int,input().split())
array=[]
value=[]
for _ in range(N):
    array.append(list(map(int,sys.stdin.readline().split())))
array.sort()

while True:
    for i in range(N):
