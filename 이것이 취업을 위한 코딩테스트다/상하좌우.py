import sys
N=int(input())
array=list(sys.stdin.readline().split())
x=1
y=1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
m_type=['L','R','U','D']
for i in array:
    nx= x+dx[m_type.index(i)]
    ny= y+dy[m_type.index(i)]
    if 1<=nx<=N and 1<=ny<=N:
        x = nx
        y = ny
print(x,y)