#2108 통계학
import sys
from collections import Counter
input = sys.stdin.readline
N=int(input())
array=[]
for _ in range(N):
    array.append(int(input()))
array.sort()

print(round(sum(array)/len(array)))
print(array[len(array)//2])
if len(array)>1:
    k= Counter(array).most_common(2)
    if k[0][1] == k[1][1]:
        print(k[1][0])
    else:
        print(k[0][0])
else:
    print(array[0])
print(max(array)-min(array))
