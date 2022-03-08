#1018 체스판 다시 칠하기
import sys
N, M = map(int,input().split())
chess=[]
for i in range(N):
    chess.append(list(input()))
carr=[]
starts=[]
color=[ 'W', 'B']
for i in range(N-7):
    for j in range(M-7):
        starts.append([i,j])
for start in starts:
    i=start[0]
    j=start[1]
    cnt=0
    fir = color.index(chess[i][j])
    nex = 1 - fir
    if (i+j+2)%2==0:
        for m in range(i,i+8):
            for n in range(j,j+8):
                if (m+n+2)%2==0:
                    if color.index(chess[m][n])!= fir:
                        cnt+=1
                else:
                    if color.index(chess[m][n]) != nex:
                        cnt+=1
    else:
        for m in range(i,i+8):
            for n in range(j,j+8):
                if (m+n+2)%2!=0:
                    if color.index(chess[m][n])!= fir:
                        cnt+=1
                else:
                    if color.index(chess[m][n]) != nex:
                        cnt+=1
    carr.append(cnt)
    cnt=0
    if (i+j+2)%2==0:
        for m in range(i,i+8):
            for n in range(j,j+8):
                if (m+n+2)%2==0:
                    if color.index(chess[m][n])== fir:
                        cnt+=1
                else:
                    if color.index(chess[m][n]) == nex:
                        cnt+=1
    else:
        for m in range(i,i+8):
            for n in range(j,j+8):
                if (m+n+2)%2!=0:
                    if color.index(chess[m][n])== fir:
                        cnt+=1
                else:
                    if color.index(chess[m][n]) == nex:
                        cnt+=1
    carr.append(cnt)

print(min(carr))
