#11651 좌표정렬하기2

import sys
input=sys.stdin.readline

array=[list(map(int,input().split())) for _ in range(int(input()))]

array.sort(key=lambda x: (x[1], x[0]))

for i in array:
    print(*i)