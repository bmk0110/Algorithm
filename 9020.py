#9020 골드바흐의 추측
# sosu=[]
# for i in range(2,10000):
#     error=0
#     for j in range(2, int(i**0.5)+1):
#         if i % j ==0:
#             error=1
#             break
#     if error==0:
#         sosu.append(i)
#
# T = int(input())
# for _ in range(T):
#     N= int(input())
#     array=[]
#     for i in range(2,int(N/2)+1 ):
#         if i in sosu and N-i in sosu:
#             array.append([i,N-i])
#
#     print(array[len(array)-1][0], end= ' ')
#     print(array[len(array)-1][1])


number=[]
T = int(input())
for _ in range(T):
    number.append(int(input()))

sosu=[]
for i in range(2,max(number)+1):
    error=0
    for j in range(2, int(i**0.5)+1):
        if i % j ==0:
            error=1
            break
    if error==0:
        sosu.append(i)

for N in number:
    array=[]
    for i in range(2,int(N/2)+1 ):
        if i in sosu and N-i in sosu:
            array.append([i,N-i])

    print(array[len(array)-1][0], end= ' ')
    print(array[len(array)-1][1])