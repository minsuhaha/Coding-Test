'''
2 : 불 / 1 : 방화벽 / 0 : 빈칸
'''
import sys, copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(fire):
    graph_copy = copy.deepcopy(graph)
    for x, y in fire:
        graph_copy[x][y] = 1
    
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph_copy[nx][ny] == 0:
                    graph_copy[nx][ny] = 1
                    queue.append((nx, ny))
    safe = 0
    for i in range(n): 
        for j in range(m):
            if graph_copy[i][j] == 0:
                safe += 1
    
    return safe

firewall = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            firewall.append((i, j))

max_safe = 0
for comb in combinations(firewall, 3):
    max_safe = max(max_safe, bfs(comb))
print(max_safe)