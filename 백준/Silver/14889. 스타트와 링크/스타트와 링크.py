import sys
input = sys.stdin.readline
INF = float('inf')

def dfs(node, cnt):
    global min_diff
    if n // 2 == cnt:
        team1, team2 = 0, 0
        
        # team1 
        for i in range(1, n+1):
            for j in range(i, n+1):
                if visited[i] and visited[j]:
                    team1 += graph[i-1][j-1] + graph[j-1][i-1]
        
        # team2
        for i in range(1, n+1):
            for j in range(i, n+1):
                if not visited[i] and not visited[j]:
                    team2 += graph[i-1][j-1] + graph[j-1][i-1]

        min_diff = min(min_diff, abs(team1-team2))
        return
    
    for i in range(node+1, n+1):
        visited[i] = True
        dfs(i, cnt+1)
        visited[i] = False

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

min_diff = INF
visited = [False] * (n+1)
for i in range(1, n+1):
    visited[i] = True
    dfs(i, 1)
    visited[i] = False

print(min_diff)
