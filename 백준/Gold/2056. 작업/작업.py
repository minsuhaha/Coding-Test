import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    end_time = [0] * (n+1)

    while queue:
        node = queue.popleft()
        end_time[node] += check[node][0]

        for next_node in graph[node]:
            check[next_node][1] -= 1
            end_time[next_node] = max(end_time[next_node], end_time[node])
            if check[next_node][1] == 0:
                queue.append(next_node)

    return max(end_time)

n = int(input())
graph = [[] for _ in range(n+1)]
check = [] * (n+1) # (걸리는시간, 선행작업 수)
check.append([0, 0])

for i in range(1, n+1):
    lst = list(map(int, input().split()))
    if lst[1] != 0:
        for job in lst[2:]:
            graph[job].append(i)
    check.append([lst[0], lst[1]])

queue = deque()
for i in range(1, n+1):
    if check[i][1] == 0:
        queue.append(i)

print(bfs())
