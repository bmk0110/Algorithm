#뒤집기
a=list(input())
cnt1=0
cnt0=0
if a[0]=='0':
    cnt0+=1
else:
    cnt1+=1

for i in range(1,len(a)):
    if a[i]!= a[i-1]:
        if a[i]=='0':
            cnt0 += 1
        else:
            cnt1 += 1
print(min(cnt0,cnt1))