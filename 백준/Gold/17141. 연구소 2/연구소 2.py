'''
문제
0 : 빈칸
1 : 벽
2 : 바이러스를 놓을 수 있는 칸
* 승원이는 연구소의 특정 위치에 바이러스 M개를 놓음

결론
- M개의 바이러스로 연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력
- 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력
'''
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(virus_comb):
    queue = deque()
    visited = [[-1]*N for _ in range(N)]

    for comb in virus_comb:
        queue.append((comb[1], comb[0]))
        visited[comb[0]][comb[1]] = 0
    
    time = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N:
                if visited[ny][nx] == -1:
                    if graph[ny][nx] == 0 or graph[ny][nx] == 2:
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append((nx, ny))
                        time = visited[ny][nx]
    
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 1 and visited[i][j] == -1:
                return -1
    return time
    
                
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

virus = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            virus.append((i, j))

ans = []
time = 0
for virus_comb in combinations(virus, M):
    time = bfs(virus_comb)
    if time >= 0:
        ans.append(time)
    
if ans:
    print(min(ans))
else:
    print(-1)
