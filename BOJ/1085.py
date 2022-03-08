#1085 직사각형에서 탈출

import sys

x,y,w,h = map(int, sys.stdin.readline().split())
array=[x,y,w-x,h-y]
print(min(array))