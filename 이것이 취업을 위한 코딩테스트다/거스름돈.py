N= int(input())

cnt=0

ctype=[500,100,50,10]

for c in ctype:
    cnt += N//c
    N %= c
print(cnt)



