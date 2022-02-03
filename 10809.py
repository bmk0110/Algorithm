#10809 알파벳찾기

alpha=list('abcdefghijklmnopqrstuvwxyz')
array=[-1 for _ in range(len(alpha))]
N=list(map(str, input()))

for i in range(len(N)):
    if array[alpha.index(N[i])] == -1:
        array[alpha.index(N[i])] = i

for j in array:
    print(j, end=' ')

