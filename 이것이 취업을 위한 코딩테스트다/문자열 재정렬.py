import sys
input=sys.stdin.readline
S = list(input().rstrip())
cnt=0
arr=[]
for i in range(len(S)):
    if S[i].isalpha():
        arr.append(S[i])
    else:
        cnt+=int(S[i])
arr.sort()
arr.append(str(cnt))
print(''.join(arr))
#K1KA5CB7