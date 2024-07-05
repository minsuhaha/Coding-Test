import sys
from collections import deque
input = sys.stdin.readline


def bfs(x):
    queue = deque([x])
    second = 100001
    case = 0

    while queue:
        x = queue.popleft()
        
        if dist[x] > second:
            break

        if x == K:
            second = dist[x]
            case += 1    

        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= 100000 and (dist[nx] == dist[x] + 1 or dist[nx] == 0) :
                queue.append(nx)
                dist[nx] = dist[x] + 1

    return second, case

N, K = map(int, input().split())
dist = [0] * 100001
second, case = bfs(N)
print(second)
print(case)

