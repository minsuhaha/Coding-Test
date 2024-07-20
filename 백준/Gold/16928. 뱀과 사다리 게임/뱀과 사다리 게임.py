import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

bridge = {}
for _ in range(N):
    x, y = map(int, input().split())
    bridge[x] = y

snake = {}
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v

def bfs(x):
    queue = deque([x])
    visited[x] = True

    while queue:
        x = queue.popleft()

        if x == 100:
            return

        for i in range(1, 7):
            next_num = x+i
            
            if next_num <= 100 and not visited[next_num]:
                if next_num in bridge.keys():
                    next_num = bridge[next_num]

                if next_num in snake.keys():
                    next_num = snake[next_num]

                if not visited[next_num]:
                    nums[next_num] = nums[x] + 1
                    visited[next_num] = True
                    queue.append(next_num)

visited = [False] * 101
nums = [0] * 101
bfs(1)
print(nums[100])
