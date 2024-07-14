import sys
import copy
from collections import deque
input = sys.stdin.readline


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def back(cnt):
    global count
    if cnt == 3:    
        count = max(bfs(), count)
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1 # 벽으로 만들어주기
                cnt += 1
                back(cnt)
                graph[i][j] = 0
                cnt -= 1

def bfs():
    queue = deque()

    graph_copy = copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if graph_copy[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if graph_copy[nx][ny] == 0:
                    graph_copy[nx][ny] = 2 # 바이러스 퍼짐
                    queue.append((nx, ny))
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph_copy[i][j] == 0:
                cnt += 1
    
    if cnt:
        return cnt
    return 0

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
count = 0
back(0)
print(count)
