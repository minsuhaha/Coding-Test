import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n:
                if nx == r2 and ny == c2:
                    return visited[x][y] + 1
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return -1

n = int(input())
graph = [[0]*n for _ in range(n)]
r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

visited = [[-1]*n for _ in range(n)]
print(bfs(r1, c1))
