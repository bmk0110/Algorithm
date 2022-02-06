#4153 직각삼각형
while True:
    array=list(map(int,input().split()))
    array.sort()
    if array==[0,0,0]:
        break
    else:
        if array[0]**2+array[1]**2==array[2]**2:
            print('right')
        else:
            print("wrong")