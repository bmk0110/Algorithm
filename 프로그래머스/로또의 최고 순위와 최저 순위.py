# def solution(lottos, win_nums):
#     cnt=0
#     for i in lottos:
#         if i in win_nums:
#             cnt+=1
#     result=[]
#     if cnt==0:
#         result.append(6)
#     else:
#         result.append(7-cnt)
#     if cnt+lottos.count(0) == 0:
#         result.append(6)
#     else:
#         result.append(7-cnt-lottos.count(0))
#     result.sort()
#     answer=[min(result),max(result)]
#     return answer


# def solution(lottos, win_nums):
#     cnt = 0
#     for l in lottos:
#         if l in win_nums:
#             cnt += 1
#     zc = lottos.count(0)
#     answer = []
#     if cnt + zc == 0:
#         answer.append(6)
#     else:
#         answer.append(7 - cnt - zc)
#     if 1 >= cnt:
#         answer.append(6)
#     if cnt > 1:
#         answer.append(7 - cnt)
#
#     return answer
