def solution(fees, records):
    ina = []
    outa = []
    for record in records:
        if 'IN' in record:
            ina.append(record.split())
        if 'OUT' in record:
            outa.append(record.split())
    isout = [False] * len(ina)
    used = [False] * len(outa)
    array = dict()
    for i in ina:
        array[i[1]] = 0
    for i in range(len(ina)):
        cnt = 0
        for j in range(len(outa)):
            if ina[i][1] == outa[j][1] and used[j] == False:
                cnt = (int(outa[j][0][0:2]) - int(ina[i][0][0:2])) * 60 + (int(outa[j][0][3:5]) - int(ina[i][0][3:5]))
                array[ina[i][1]] += cnt
                used[j] = True
                isout[i] = True
                break
        if isout[i] == False:
            cnt = (23 - int(ina[i][0][0:2])) * 60 + (59 - int(ina[i][0][3:5]))
            array[ina[i][1]] += cnt
    array = sorted(array.items())
    answer = []
    for i in array:
        answer.append(feecount(i[1],fees))
    return answer

def feecount(cnt, f):
    if cnt <= f[0]:
        return f[1]
    else:
        k = (cnt - f[0]) // f[2]
        if (cnt - f[0]) % f[2] != 0:
            k += 1
        return f[1] + k * f[3]