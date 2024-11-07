from collections import deque
def solution(n, results):
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    
    for v1, v2 in results:
        win[v1].append(v2)
        lose[v2].append(v1)
    
    def bfs(node, graph):
        queue = deque([node])
        visited[node] = True
        
        while queue:
            node = queue.popleft()
            
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
    ans = 0
    for i in range(1, n+1):
        visited = [False] * (n+1)
        bfs(i, win)
        bfs(i, lose)
        cnt = 0
        for v in visited:
            if v:
                cnt += 1
        if cnt == n:
            ans+=1
    return ans