#11653 소인수분해

N = int(input())
if N>1:
    while N!=1:
        for i in range(2,N+1):
            if N % i == 0:
                N //= i
                print(i)
                break