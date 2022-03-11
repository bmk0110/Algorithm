#1181 단어정렬

import sys
input=sys.stdin.readline
array=[]
for _ in range(int(input())):
    array.append(input().rstrip())
array=list(set(array))
array.sort(key=lambda x: (len(x), x))

for i in array:
    print(''.join(map(str,i)))