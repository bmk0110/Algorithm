#11650 좌표 정렬하기
import sys
input=sys.stdin.readline

array=[list(map(int,input().split())) for _ in range(int(input()))]

array.sort(key=lambda x: (x[0], x[1]))

for i in array:
    print(*i)