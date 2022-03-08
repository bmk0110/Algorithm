#3036 링
import sys
N = int(input())
array=list(map(int,sys.stdin.readline().split()))
for j in range(1,len(array)):
    i=array[0]
    while True:
        if array[0]%i ==0 and array[j]%i==0:
            minv=i
            break
        else:
            i-=1
    print(f'{array[0]//minv}/{array[j]//minv}')