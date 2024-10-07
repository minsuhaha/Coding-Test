'''
문제 
- tree 형태로 주어짐
- 사이클이 더 이상 존재 하지 않은 때 까지 cnt + 1
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node):
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[node] = True
            dfs(next_node)
            dp[node][0] += dp[next_node][1]
            dp[node][1] += min(dp[next_node])

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 1] for _ in range(n+1)] # 0: 얼리어답터x / 1: 얼리어답터
visited = [False] * (n+1)
visited[1] = True
dfs(1)
print(min(dp[1]))
