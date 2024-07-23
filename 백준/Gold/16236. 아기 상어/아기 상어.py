import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0 , 0]
dy = [0, 0, -1, 1]

def bfs(x, y, size):
    queue = deque([(x, y, 0)])
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True
    lst = []

    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if graph[nx][ny] < size and graph[nx][ny] !=0: # 빈칸이 아니면서 아기상어 사이즈보다 작은 물고기
                    visited[nx][ny] = True
                    lst.append((nx, ny, dist+1))
                elif graph[nx][ny] == size or graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist+1))
                
    return sorted(lst, key=lambda x:(x[2], x[0], x[1]))


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            x, y = i, j
            break

time, size = 0, 2
eat = 0
while True:
    res = bfs(x, y, size)

    if len(res) == 0:
        print(time)
        break

    nx, ny, dist = res[0]

    graph[x][y], graph[nx][ny] = 0, 9
    x, y = nx, ny

    time += dist
    eat += 1

    if eat == size:
        size += 1
        eat = 0
    