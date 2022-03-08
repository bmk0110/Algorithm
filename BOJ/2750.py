#2750 수 정렬하기
array=[]
N=int(input())
for i in range(N):
    a =int(input())
    if a not in array:
        array.append(a)
array.sort()
for i in array:
    print(i)