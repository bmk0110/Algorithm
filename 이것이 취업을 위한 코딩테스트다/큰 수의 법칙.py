import sys

N, M, K = map(int,sys.stdin.readline().split())
array=list(map(int,sys.stdin.readline().split()))
array.sort(reverse=True)

fst = array[0]
snd = array[1]
# result=0
# cnt = 0

# while cnt<M:
#     for _ in range(K):
#         result+=fst
#         cnt+=1
#         if cnt==M:
#             break
#     result+=snd
#     cnt+=1

cnt = (M//(K+1))*K+M%(K+1)
result = fst*cnt + snd*(M-cnt)

print(result)