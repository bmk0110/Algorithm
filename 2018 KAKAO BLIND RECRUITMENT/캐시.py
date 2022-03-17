cacheSize = 3
cities =["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

def solution(cacheSize, cities):
    answer=0
    array = []
    if cacheSize==0:
        return len(cities)*5
    else:
        for i in cities:
            if len(array) <cacheSize:
                if i.upper() in array:
                    array.append(array.pop(array.index(i.upper())))
                    answer+=1
                else:
                    array.append(i.upper())
                    answer+=5
            else:
                if i.upper() in array:
                    array.append(array.pop(array.index(i.upper())))
                    answer+=1
                else:
                    array.pop(0)
                    array.append(i.upper())
                    answer+=5
        return answer

print(solution(cacheSize,cities))
