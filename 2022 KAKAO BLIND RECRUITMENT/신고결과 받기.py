def solution(id_list, report, k):
    final = [0] * len(id_list)
    array = {id: [] for id in id_list}
    reports = {id: 0 for id in id_list}

    for i in set(report):
        user = i.split(" ")
        array[user[0]].append(user[1])
        reports[user[1]] += 1

    for key, value in array.items():
        for v in value:
            if reports[v] >= k:
                final[id_list.index(key)] += 1
    return final