#3190 뱀
import sys

N = int(input())
head = [0,0]
tail = [0,0]
A = int(input())
array = [[0]*N for _ in range(N)]

direct=[]

dx= [-1,1,0,0]

for _ in range(A):
    a, b = (map(int, sys.stdin.readline().split()))
    array[a-1][b-1]=1
L = int(input())
for _ in range(L):
    direct.append(list(sys.stdin.readline().split()))

while True:
    head[0]+=1
    head[1]+=1

print(array)
print(direct)

