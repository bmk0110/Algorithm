#2609 최대공약수와 최소공배수

array = list(map(int,input().split()))
array.sort()
i=array[0]
while True:
    if array[0]%i ==0 and array[1]%i==0:
        minv=i
        break
    else:
        i-=1
j=1
while True:
    if (array[0] * j)%array[1] == 0 :
        maxv=array[0] * j
        break
    else:
        j+=1

print(minv)
print(maxv)