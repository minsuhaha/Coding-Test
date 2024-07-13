import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited[x][y][0] = 1

    while queue:
        x, y, k = queue.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][k]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0 and not visited[nx][ny][k]:
                    visited[nx][ny][k] = visited[x][y][k] + 1
                    queue.append((nx, ny, k))
                
                elif graph[nx][ny] == 1 and k < K and not visited[nx][ny][k+1]:
                    visited[nx][ny][k+1] = visited[x][y][k] + 1
                    queue.append((nx, ny, k+1))
    return -1

N, M, K = map(int, input().split())
graph = [list(map(int, input()))for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
print(bfs(0, 0))
