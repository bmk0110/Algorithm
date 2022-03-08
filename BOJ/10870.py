#10870 피보나치 수 5

def fibo(a):
    global fst,snd,cnt
    cnt= fst+snd
    if a<n:
        fst=snd
        snd=cnt
        fibo(a+1)
n = int(input())
cnt=0
fst=0
snd=1
if n<=1:
    print(n)
else:
    fibo(2)
    print(cnt)