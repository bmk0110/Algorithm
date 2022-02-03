#2675 문자열 반복

T = int(input())
for t in range(T):
    R, S = map(str,input().split())
    array = list(S)
    R = int(R)
    for i in range(len(array)):
        print(array[i]*R, end='')
    print()