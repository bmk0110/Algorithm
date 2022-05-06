from itertools import combinations_with_replacement

def solution(n, info):
    answer=[-1]
    max_score=0
    for arrow in list(combinations_with_replacement(range(0, 11), n)):
        score=[0 for _ in range(11)]
        for a in arrow:
            score[10-a]+=1
        apeach=0
        lion=0
        for i in range(11):
            if info[i]>=score[i]:
                if info[i]>0:
                    apeach+=(10-i)
            else:
                lion +=(10-i)
        if lion>apeach:
            if max_score<lion-apeach:
                max_score=lion-apeach
                answer=score
            elif max_score==lion-apeach:
                for i in range(10, -1, -1):
                    if answer[i]>score[i]:
                        break
                    elif score[i]>answer[i]:
                        max_score = lion-apeach
                        answer = score
                        break
    return answer

n= 5
info= [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n,info))
