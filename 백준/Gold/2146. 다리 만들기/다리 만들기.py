import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, num):
    queue = deque([(x, y)])
    graph[x][y] = num # 방문표시

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = num
                queue.append((nx, ny))

def check(z):
    queue = deque([])
    visited = [[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if graph[i][j] == z:
                queue.append((i, j, 0))

    while queue:
        x, y, k = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1:
                continue
            
            # 다른 육지 일때
            if graph[nx][ny] > 1 and graph[nx][ny] != z:
                return k
            
            # 바다 일때
            if graph[nx][ny] == 0 and not visited[nx][ny]:
                queue.append((nx, ny, k+1))
                visited[nx][ny] = True

    return INF

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

num = 2 # 임의의 유지 번호
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j, num)
            num += 1 

ans = INF
for i in range(2, num):
    ans = min(check(i), ans)

print(ans)
