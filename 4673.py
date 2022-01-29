
array=[0 for _ in range(10001)]
# print(array)
for i in range(1,10001):
    s = 0
    s+=i
    for j in str(i):
        s+=int(j)
    if s<=10000:
        array[s]= 1
for i in range(1,10001):
    if array[i]==0:
        print(i)