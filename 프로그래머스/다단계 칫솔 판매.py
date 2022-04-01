enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral=["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller=["young", "john", "tod", "emily", "mary"]
amount=[12, 4, 2, 5, 10]



def solution(enroll, referral, seller, amount):
    final={}
    for name in enroll:
        final[name] = [0]
    for i in range(len(referral)):
        final[enroll[i]].append(referral[i])

    for i in range(len(seller)):
        arr=[]
        arr.append(seller[i])
        cash = amount[i]*100
        while arr:
            if cash==0:
                break
            a=arr.pop()
            if final[a][1] == '-' :
                final[a][0]+=cash- cash//10
            else:
                final[a][0]+=cash- cash//10
                cash= cash//10
                arr.append(final[a][1])
    answer = []

    for i in final:
        answer.append(final[i][0])
    return answer



print(solution(enroll, referral, seller, amount))


