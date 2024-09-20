'''
1. 상하좌우 4방향으로 이동가능
2. 6자리 수 만들기
3. 중복 X -> set 사용
'''
import sys
input = sys.stdin.readline

graph = [list(input().split()) for _ in range(5)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, res):
    if len(res) == 6:
        num_set.add(res)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<5 and 0<=ny<5:
            dfs(nx, ny, res+graph[nx][ny])

num_set = set()
for i in range(5):
    for j in range(5):
        dfs(i, j, graph[i][j])
print(len(num_set))
