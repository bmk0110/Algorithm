import math
def solution(n, k):
    tmp = ''
    while n:
        tmp += str(n % k)
        n //= k
    numb = tmp[::-1]
    array = []
    array = list(numb.replace('0', ' ').split())
    cnt = 0
    for ar in array:
        if int(ar) != 1:
            pr = True
            for i in range(2, int(math.sqrt(int(ar))) + 1):
                if int(ar) % i == 0:
                    pr = False
                    break
            if pr == True:
                cnt += 1
        else:
            pass
    return cnt