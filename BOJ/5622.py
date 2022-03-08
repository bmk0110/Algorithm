#5622 다이얼

dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
N = list(input())
array=[]
for i in range(len(N)):
    for j in range(len(dial)):
        if N[i] in dial[j]:
            array.append(j+3)
            break
print(sum(array))