def solution(s):
    arr = [len(s)]
    for i in range(1,len(s)//2 +1 ):
        st = ''
        start=s[0:i]
        cnt = 1

        for j in range(i,len(s),i):
            if s[j:j+i] == start:
                cnt+=1
            else:
                if cnt>=2:
                    st+= str(cnt)+start
                    start=s[j:j+i]
                    cnt=1
                else:
                    st+=start
                    start = s[j:j + i]
        if cnt >= 2:
            st += str(cnt) + start
        else:
            st += start
        arr.append(len(st))
    return min(arr)


print(solution(s))