import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, z):
    queue = deque([(x, y, z)])
    visited[x][y][z] = 1
    
    while queue:
        x, y, z = queue.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][z]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                continue
            
            # 이동 가능 한 칸이라면 (벽을 이미 부셨는지 여부 상관없이)
            if graph[nx][ny] == 0 and visited[nx][ny][z] == 0: # 해당 칸은 이동 할 수 있으면 아직 방문하지 않음
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
            
            # 벽을 부술 수 있는 상황이라면
            elif graph[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][z] + 1
                queue.append((nx, ny, 1))
    return -1

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)]for _ in range(N)]
 # Z = 0 : 벽을 아직 안 부수고 이동 중 / Z = 1 : 벽을 이미 한개 부시고 이동 중

res = bfs(0, 0, 0)
print(res)
