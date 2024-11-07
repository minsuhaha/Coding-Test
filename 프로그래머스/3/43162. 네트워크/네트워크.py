from collections import deque
def solution(n, computers):
    
    def bfs(node):
        queue = deque([node])
        visited[node] = True

        while queue:
            node = queue.popleft()
            
            for next_node, connect in enumerate(computers[node]):
                if not visited[next_node] and connect:
                    visited[next_node] = True
                    queue.append(next_node)
        return 1
    
    visited = [False] * n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            cnt += bfs(i)
    return cnt