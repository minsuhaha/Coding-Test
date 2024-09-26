'''
문제
 0 : 이동 가능 칸
 1 : 벽
* 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동 가능

결론
(1, 1) -> (N, M) 이동하는데 최단거리
'''
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited[y][x][0] = 1

    while queue:
        x, y, z = queue.popleft()

        if x == m-1 and y == n-1:
            return visited[y][x][z]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n:
                if not visited[ny][nx][z]:
                    if graph[ny][nx] == '0':
                        visited[ny][nx][z] = visited[y][x][z] + 1
                        queue.append((nx, ny, z))

                    elif graph[ny][nx] == '1' and z == 0:
                        visited[ny][nx][1] = visited[y][x][z] + 1
                        queue.append((nx, ny, z+1))

    return -1    

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

print(bfs(0, 0))
