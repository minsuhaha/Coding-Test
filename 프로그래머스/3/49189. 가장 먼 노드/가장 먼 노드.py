from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for e1, e2 in edge:
        graph[e1].append(e2)
        graph[e2].append(e1)
    
    def bfs(start, cnt):
        queue = deque([(start,cnt)])
        visited[start] = 1
        
        while queue:
            node, cnt = queue.popleft()
            
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = visited[node] + 1
                    queue.append((next_node, cnt+1))
        
        return cnt
    
    visited = [0] * (n+1)
    cnt = bfs(1, 1)
    return visited.count(cnt)
    
    
    
    
        