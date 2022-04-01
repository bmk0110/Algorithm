from collections import deque

def solution(rows, columns, queries):
    answer = []
    arr=[[0]*columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            arr[i][j]=i*columns +j+1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for q in queries:
        a= q[0]-1
        b= q[1]-1
        c= q[2]-1
        d= q[3]-1
        visited = [[0] * columns for _ in range(rows)]
        direction = 0
        queue = deque()
        queue.append([a, b])
        next = arr[a][b]
        final=[arr[a][b]]
        while queue:
            x, y = queue.popleft()

            nx = x + dx[direction]
            ny = y + dy[direction]
            if a <= nx <= c and b <= ny <= d and visited[nx][ny] == 0:
                final.append(arr[nx][ny])
                queue.append([nx,ny])
                next, arr[nx][ny] = arr[nx][ny],next
                visited[nx][ny]=1
            if nx+dx[direction]>c or nx+ dx[direction]<a or ny+ dy[direction]<b or ny+ dy[direction]>d:
                direction+=1
            if direction==4:
                break
        answer.append(min(final))
    return answer



rows= 6
columns=6
queries=[[2,2,5,4],[3,3,6,6],[5,1,6,3]]

print(solution(rows,columns,queries))