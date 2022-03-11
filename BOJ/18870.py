#18870 좌표압축

import sys
input=sys.stdin.readline
N=int(input())
array=list(map(int,input().split()))
k=list(set(array))
k.sort()
dic = {k[i]:i for i in range (len(k))}

for i in array:
    print(dic[i],end=' ')