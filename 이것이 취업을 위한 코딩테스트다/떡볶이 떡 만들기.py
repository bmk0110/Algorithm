import sys
input = sys.stdin.readline
def bs(array,target,start,end):
    while start<=end:
        total=0
        mid= (start+end)//2
        for r in Rice:
            if r>mid:
                total+= (r-mid)
        if total==M:
            return mid
        elif total>M:
            start= mid+1
        elif total<M:
            end= mid-1

N, M = map(int,input().split())
Rice= list(map(int,input().split()))
result=bs(Rice, 6, 0, max(Rice))
print(result)