#5086 배수와 약수
while True:
    a, b = map(int,input().split())
    if (a,b)==(0,0):
        break
    else:
        if a<b:
            print('factor')
        elif a%b==0:
            print('multiple')
        else:
            print('neither')
