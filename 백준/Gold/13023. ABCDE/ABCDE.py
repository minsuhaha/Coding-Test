import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)] # node 번호가 0부터 시작이고 N-1까지 있기에 그냥 n으로 for
visited = [False] * n
result = False

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(i, depth):
    visited[i] = True
    if depth == 5:
        global result
        result = True
        return
    
    for node in graph[i]:
        if not visited[node]: # 이전에 나왔던 친구가 아니면
            dfs(node, depth+1)
            visited[node] = False

for i in range(n):
    dfs(i, 1)
    visited[i] = False
    
    if result:
        break

if result:
    print(1)
else:
    print(0)