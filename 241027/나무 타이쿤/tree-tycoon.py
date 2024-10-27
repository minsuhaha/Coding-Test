import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
queue = deque([(n-2, 0), (n-1, 0), (n-2, 1), (n-1, 1)]) # 초기 특수 영양제 초기화
# visited = [[False]*n for _ in range(n)]

# m만큼 반복
for _ in range(m):
    d, p = map(int, input().split())

    # 1. 이동규칙에 따라 특수영양제 이동 / 특수 영양제 투입
    move_queue = deque()
    while queue:
        x, y = queue.popleft()
        nx = (x + move[d-1][0]*p) % n
        ny = (y + move[d-1][1]*p) % n

        move_queue.append((nx, ny))
        graph[nx][ny] += 1
    
    
    # 2. 특수영양제를 투입 한 리브로수의 대각선 방향 파악 / 특수영양제 제거
    for x, y in move_queue:
        # d -> 1, 3, 5, 7
        for i in range(1, 8, 2):
            nx = x + move[i][0]
            ny = y + move[i][1]

            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                continue

            if graph[nx][ny] >= 1:
                graph[x][y] += 1

    # 3. 특수영양제 방금 투입 한 곳 제외 2이상 리브로수 -2해주고 특수영양제 놓기
    visited = set(move_queue)
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited and graph[i][j] >= 2:
                graph[i][j] -= 2
                queue.append((i, j))

print(sum(map(sum, graph)))