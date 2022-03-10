import sys

array = list(input())
final=int(array[0])
for i in range(1,len(array)):

    if int(array[i])!=0 and final !=0:
        final*=int(array[i])
    else:
        final+=int(array[i])
print(final)
