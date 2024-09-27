'''
문제
0 : 이동가능
1 : 벽
* 도중에 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 K개 까지 부수고 이동

결론
(1, 1)에서 (N, M)의 위치까지 이동 -> 최단거리 구하기

'''
import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y, z):
    queue = deque([(x, y, z)])
    visited[y][x][z] = 1

    while queue:
        x, y, z = queue.popleft()

        if x == M-1 and y == N-1:
            return visited[y][x][z]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<M and 0<=ny<N:
                if graph[ny][nx] == 1 and z < K and not visited[ny][nx][z+1]:
                    visited[ny][nx][z+1] = visited[y][x][z] + 1
                    queue.append((nx, ny, z+1))
                elif graph[ny][nx] == 0 and not visited[ny][nx][z]:
                    visited[ny][nx][z] = visited[y][x][z] + 1
                    queue.append((nx, ny, z))
    return -1

N, M, K = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
print(bfs(0, 0, 0))
