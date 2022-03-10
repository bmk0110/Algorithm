from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for c in course:
        array = []
        for i in orders:
            for comb in combinations(i, c):
                array.append(''.join(sorted(comb)))
                array.sort()
        if len(array)>0:
            k=Counter(array).most_common()
            if k[0][1]>=2:
                for i in k:
                    if i[1]==k[0][1]:
                       answer.append(i[0])
    answer.sort()
    return answer