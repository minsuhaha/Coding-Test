from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    def bfs(node):
        queue = deque([node])
        visited[node] = 0
        
        while queue:
            now_node = queue.popleft()
            
            for next_node in graph[now_node]:
                if visited[next_node] == -1:
                    visited[next_node] = visited[now_node] + 1
                    queue.append(next_node)
                    
        return visited[now_node]    
    
    visited = [-1] * (n+1)
    max_length = bfs(1)
    cnt = 0
    for i in range(1, n+1):
        if visited[i] == max_length:
            cnt += 1
    return cnt