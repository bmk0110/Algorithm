#1655 가운데를 말해요

N = int(input())
array =[]
for _ in range(N):

    jjaksu=[]
    array.append(int(input()))
    array.sort()
    # print('array = ', array)
    if len(array)%2==1:
        # print('홀수일때')
        print(array[len(array)//2])
    else:
        jjaksu.append(array[(len(array)//2)])
        jjaksu.append(array[(len(array)//2)-1])
        # print('짝수일때')
        # print(jjaksu)
        print(min(jjaksu))
