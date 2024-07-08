import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

monkey_x = [-2, -1, 1, 2, 2, 1, -1, -2]
monkey_y = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y, k):
    queue = deque([(x, y, k)])
    
    while queue:
        x, y, k = queue.popleft()

        if x == W-1 and y == H-1:
            return visited[y][x][k]
        
        if k < K:    
            for i in range(8):
                mx = x + monkey_x[i]
                my = y + monkey_y[i]

                if mx < 0 or mx > W-1 or my < 0 or my > H-1:
                    continue

                if graph[my][mx] == 0 and visited[my][mx][k+1] == 0:
                    visited[my][mx][k+1] = visited[y][x][k] + 1
                    queue.append((mx, my, k+1))

        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > W-1 or ny < 0 or ny > H-1:
                continue

            if graph[ny][nx] == 0 and not visited[ny][nx][k]:
                visited[ny][nx][k] = visited[y][x][k] + 1
                queue.append((nx, ny, k))
    return -1

K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]
visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
print(bfs(0, 0, 0))
