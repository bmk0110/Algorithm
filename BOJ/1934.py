#1934 최소공배수

T = int(input())
for _ in range(T):
    array = list(map(int,input().split()))
    array.sort()
    j=1
    while True:
        if (array[0] * j)%array[1] == 0 :
            maxv=array[0] * j
            break
        else:
            j+=1
    print(maxv)