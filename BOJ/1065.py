#1065 한수

N = int(input())
cnt=0
for i in range(1,N+1):
    array= []
    carray=[]
    if len(str(i))==1:
        cnt+=1
    else:
        for j in str(i):
            array.append(int(j))
        for j in range(len(array)-1):
            carray.append(array[j+1]-array[j])
        carray=set(carray)
        if len(carray)==1:
            cnt+=1
print(cnt)
