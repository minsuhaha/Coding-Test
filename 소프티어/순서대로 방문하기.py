import sys

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = []
for _ in range(m):
    x, y = map(int, input().split())
    move.append((x-1, y-1))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(start, depth):
    global cnt
    if start == move[depth]:
        if depth == m-1:
            cnt += 1
            return
        else:
            depth += 1

    x, y = start
    visited[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and graph[nx][ny] == 0:
                dfs((nx, ny), depth)
    visited[x][y] = False

    
cnt = 0
visited = [[False]*n for _ in range(n)]
visited[move[0][0]][move[0][1]] = True
dfs(move[0], 1)
print(cnt)
