#1002 터렛
import sys
T = int(input())
for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,sys.stdin.readline().split())
    xy = (abs(x1-x2)**2+abs(y1-y2)**2)**0.5

    if x1==x2 and y1==y2 and r1==r2:
        print(-1)

    elif r1+r2==xy or abs(r1-r2)==xy:
        print(1)
    elif abs(r1-r2)<xy<r1+r2:
        print(2)
    else:
        print(0)
