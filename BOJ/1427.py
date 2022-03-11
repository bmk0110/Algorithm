#1427소트인사이드
import sys

a= list(map(int,sys.stdin.readline().rstrip()))
a.sort(reverse=True)
print(''.join(map(str,a)))