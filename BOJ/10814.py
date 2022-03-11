#10814 나이순 정렬
import sys
input=sys.stdin.readline
array=[]
for i in range(int(input())):
    age, name = map(str, input().split())
    array.append([int(age),name,i])
array.sort(key=lambda x:(x[0],x[2]))
for i in array:
    print(i[0],i[1])