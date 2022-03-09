k = input()
y=ord(k[0])-ord('a')
x = int(k[1])-1
dx=[2,2,-2,-2,-1,1,-1,1]
dy=[-1,1,-1,1,2,2,-2,-2]
cnt=0
for i in range(8):
    nx = x+dx[i]
    ny = y+dy[i]
    if 0<=nx<=7 and 0<=ny<=7:
        cnt+=1
print(cnt)



