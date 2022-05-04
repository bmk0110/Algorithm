import sys


def record(start):
    a = start
    b = start + 1
    if a < 10:
        a = '0' + str(a)
    else:
        a = str(a)
    if b < 10:
        b = '0' + str(b)
    else:
        b = str(b)
    return a + '-' + b


N, M = map(int, sys.stdin.readline().split())

rooms = []
for _ in range(N):
    rooms.append([input(), 9, 10, 11, 12, 13, 14, 15, 16, 17])
rooms.sort()
reserve = []
for _ in range(M):
    a, b, c = map(str, sys.stdin.readline().split())
    reserve.append([a, int(b), int(c)])
for i in range(M):
    ind = 0
    for j in range(N):
        if rooms[j][0] == reserve[i][0]:
            ind = j
            break
    for k in range(reserve[i][1], reserve[i][2]):
        rooms[j].remove(k)
new_rooms = []
for i in range(len(rooms)):
    if len(rooms[i]) == 10:
        new_rooms.append([rooms[i][0], '09-18'])
    elif len(rooms[i]) == 1:
        new_rooms.append(rooms[i])
    elif len(rooms[i]) == 2:
        new_rooms.append([rooms[i][0], record(rooms[i][1])])
    else:
        numbers = rooms[i][1:len(rooms[i])]
        # print(numbers)
        arr = [rooms[i][0]]
        start = 0
        ss = 0
        end = 1
        finish = False
        while end < len(numbers):
            if numbers[end] - numbers[ss] == 1:
                ss += 1
                end += 1
            else:
                a = numbers[start]
                b = numbers[ss] + 1
                if a < 10:
                    a = '0' + str(a)
                else:
                    a = str(a)
                if b < 10:
                    b = '0' + str(b)
                else:
                    b = str(b)
                arr.append(a + '-' + b)
                start = end
                ss = start
                if start == len(numbers) - 1:
                    arr.append(record(numbers[start]))
                    finish = True
                    break
                else:
                    end = start + 1
        if finish != True:
            a = numbers[start]
            b = numbers[ss] + 1
            if a < 10:
                a = '0' + str(a)
            else:
                a = str(a)
            if b < 10:
                b = '0' + str(b)
            else:
                b = str(b)
            arr.append(a + '-' + b)
        new_rooms.append(arr)
for r in range(len(new_rooms)):
    if r != 0:
        print('-----')
    print('Room ' + new_rooms[r][0] + ':')
    if len(new_rooms[r]) == 1:
        print('Not available')
    else:
        print(len(new_rooms[r]) - 1, end=' ')
        print('available:')
        for i in range(1, len(new_rooms[r])):
            print(new_rooms[r][i])
