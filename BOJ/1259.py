#1259 펠린드롬수
while True:
    N = list(map(str,input()))
    if N==['0']:
        break
    else:
        k=N.copy()
        k.reverse()
        if N==k:
            print('yes')
        else:
            print('no')