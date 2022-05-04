def rotate(a):
    n = len(a)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = a[i][j]
    return result


def check(a):
    for i in range(len(a) // 3, len(a) // 3 * 2):
        for j in range(len(a) // 3, len(a) // 3 * 2):
            if a[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * 3 * n for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
    for _ in range(4):
        key = rotate(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[i + x][j + y] += key[i][j]
                if check(new_lock) == True:
                    return True
                else:
                    for i in range(m):
                        for j in range(m):
                            new_lock[i + x][j + y] -= key[i][j]

    return False
key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))