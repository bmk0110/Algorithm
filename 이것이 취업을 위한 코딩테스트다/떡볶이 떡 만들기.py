import sys
input = sys.stdin.readline

def bs(arr,target,start,end):
    result=0
    while start<=end:
        mid=(start+end)//2
        cnt=0
        for a in arr:
            if a>mid:
                cnt+= a-mid
        if cnt<target:
            end=mid-1
        else:
            result=mid
            start=mid+1
    return result

N,M= map(int,input().split())
arr=list(map(int,input().split()))
print(bs(arr,M,0,max(arr)))