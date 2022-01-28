#분해합

N= int(input())

for i in range(1, N+1):
    sums = sum(map(int, str(i)))
    sums += i
    if sums==N:
        print(i)
        break
    if i == N:
        print(0)