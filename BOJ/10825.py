#10825 국영수
import sys
array=[list(map(str, sys.stdin.readline().split())) for _ in range(int(input()))]
array.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in array:
    print(i[0])