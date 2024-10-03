import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt, num):
    global max_num
    if cnt == 4:
        max_num = max(max_num, num)
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt+1, num+graph[nx][ny])
            visited[nx][ny] = False

def dfs2(x, y):
    global max_num
    res = []
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            res.append(graph[nx][ny])

    if len(res) == 4:
        res.sort(reverse=True)
        res.pop()
        max_num = max(max_num, sum(res)+graph[x][y])
    
    elif len(res) == 3:
        max_num = max(max_num, sum(res)+graph[x][y])


max_num = 0
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        dfs2(i, j)
        visited[i][j] = False

print(max_num)
