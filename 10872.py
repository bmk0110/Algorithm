#10872 팩토리얼

def fact(a):
    global cnt
    cnt*=a
    if a-1>0:
        fact(a-1)

N = int(input())
cnt=1
if N>0:
    fact(N)
print(cnt)