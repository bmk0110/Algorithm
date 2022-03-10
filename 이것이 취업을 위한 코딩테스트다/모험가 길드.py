import sys

N = int(input())
array = list(map(int,sys.stdin.readline().split()))
array.sort()
cnt=0
final=0
for i in array:
    cnt+=1
    if cnt >=i:
        final +=1
        cnt=0
print(final)