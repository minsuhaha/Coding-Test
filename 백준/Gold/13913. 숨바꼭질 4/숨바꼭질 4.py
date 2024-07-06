import sys
from collections import deque, defaultdict
input = sys.stdin.readline

res = []
def bfs(x):
    queue = deque([x])

    while queue:
        x = queue.popleft()

        if x == K:
            res.append(K)
            m = move[K]
            for _ in range(point[x]):
                res.append(m)
                m = move[m]
            return point[x], res

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and point[nx] == 0:
                point[nx] = point[x] + 1
                queue.append(nx)
                move[nx] = x # 자신의 부모노드 저장


N, K = map(int, input().split())
point = [0] * 100001
move = [0] * 100001
d, d_lst = bfs(N)
d_lst.reverse()
print(d)
print(*d_lst)
