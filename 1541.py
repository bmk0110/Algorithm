#1541 잃어버린 괄호

array=list(input().split('-'))
num=[]
for i in array:
    if '+' in i:
        next=i.split('+')
        cnt=0
        for a in next:
            cnt+=int(a)
        num.append(cnt)
    else:
        num.append(i)
final= int(num[0])
for i in range(1,len(num)):
    final-=int(num[i])
print(final)