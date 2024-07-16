import sys
from collections import defaultdict
input = sys.stdin.readline


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y, cnt):
    global count
    count = max(count, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<R and 0<=ny<C:
            if graph[nx][ny] not in visited: # 아직 방문하지 않은 알파벳일 경우
                visited.add(graph[nx][ny])
                dfs(nx, ny, cnt+1)
                visited.remove(graph[nx][ny])

R, C = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = set()
visited.add(graph[0][0])
cnt, count = 0, 0
dfs(0, 0, cnt+1)
print(count)
