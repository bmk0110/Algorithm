N= int(input())
array=[]
for _ in range(N):
    a, b= input().split()
    array.append([a, int(b)])
array.sort(key= lambda x: x[1])
for i in range(len(array)):
    print(array[i][0],end=' ')