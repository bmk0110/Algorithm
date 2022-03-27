# #방법1
# import sys
# input = sys.stdin.readline
# N = int(input())
# A=list(map(int,input().split()))
# M=int(input())
# B=list(map(int,input().split()))
# for i in range(M):
#     if B[i] in A:
#         print('yes',end=' ')
#     else:
#         print('no',end=' ')

# #방법2(이진탐색)
# def binary_search(array,target,start,end):
#     while start<=end:
#         mid= (start+end)//2
#         if array[mid] == target:
#             return mid
#         elif array[mid]>target:
#             end= mid-1
#         elif array[mid]<target:
#             start = mid+1
#     return None
# N = int(input())
# A=list(map(int,input().split()))
# A.sort()
# M=int(input())
# B=list(map(int,input().split()))
# for i in B:
#     result=binary_search(A,i,0,N-1)
#     if result==None:
#         print('no',end=' ')
#     else:
#         print('yes',end=' ')

# #방법3 계수정렬
# N = int(input())
# array = [0]*1000001
# for i in list(map(int,input().split())):
#     array[i]=1
# M = int(input())
# B= list(map(int,input().split()))
# for i in B:
#     if array[i]==1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# import sys
# input = sys.stdin.readline
#
# def binary_search(arr,target, start,end):
#     while start<=end:
#         mid = (start+end)//2
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]>target:
#             end=mid-1
#         else:
#             start= mid+1
#     return None
# N = int(input())
# arr = list(map(int,input().split()))
# M = int(input())
# customer=list(map(int,input().split()))
# for i in customer:
#     a=binary_search(arr,i,0,N-1)
#     if a ==None:
#         print('no',end=' ')
#     else:
#         print('yes',end=' ')