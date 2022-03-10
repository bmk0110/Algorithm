#10816 숫자 카드2
import sys
input = sys.stdin.readline
N = int(input())
A= list(map(int,input().split()))

M = int(input())
B = list(map(int,input().split()))

#방법1 계수정렬
array=[0]*20000001
for i in A:
    array[i]+=1
for i in B:
    print(array[i] , end=' ')
