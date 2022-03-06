#2525 오븐 시계
import sys
A, B = map(int, sys.stdin.readline().split())
C=int(input())
hour=C//60
minute=C%60
A+=hour
B+=minute
if B>=60:
    A+=1
    B-=60
if A>=24:
    A-=24
print(A, B)