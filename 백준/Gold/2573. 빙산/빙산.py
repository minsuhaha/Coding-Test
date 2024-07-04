import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                continue
            
            # 바다가 있다면
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                if graph[x][y] >= 1:
                    graph[x][y] -= 1

            # 빙산이 있다면
            elif graph[nx][ny] >= 1 and not visited[nx][ny]:
                visited[nx][ny] = True # 방문한 빙산임을 표시
                queue.append((nx, ny))


N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

year = 0
while True:
    visited = [[False] * M for _ in range(N)]
    count = 0

    # 해당 for이 종료되면 1년이 지난 거
    for i in range(N):
        for j in range(M):
            if graph[i][j] >= 1 and not visited[i][j]:
                bfs(i, j)
                count += 1
    year += 1

    if count >= 2:
        print(year-1)
        exit()
    elif count == 0:
        print(0)
        exit()