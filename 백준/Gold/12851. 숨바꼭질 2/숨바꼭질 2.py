import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

def bfs(x):
    queue = deque([x])
    second = INF
    case = 0

    while queue:
        x = queue.popleft()

        if point[x] > second:
            break

        if x == K:
            second = point[x] # 가장 빨리 발견되는 초 second 변수에 담기
            case += 1
            continue

        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= 100000 and (point[nx] == point[x] + 1 or point[nx] == 0): # 동일한 초에 속하는 값들은 queue에 넣어줘도 됨
                queue.append(nx)
                point[nx] = point[x] + 1
    return second, case

N, K = map(int, input().split())
point = [0] * 100001
second, case = bfs(N)
print(second)
print(case)
