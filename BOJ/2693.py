#2693 N번째 큰 수
import sys
input = sys.stdin.readline

for i in range(int(input())):
    array=list(map(int,input().split()))
    array.sort(reverse=True)
    print(array[2])
