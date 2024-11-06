from collections import deque
def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    
    def bfs(node1, node2):
        queue = deque([node1])
        visited = [False] * (n+1)
        visited[node1] = True
        cnt = 0
        while queue:
            cnt += 1
            node = queue.popleft()
            for next_node in graph[node]:
                if next_node != node2 and not visited[next_node]:
                    visited[next_node] = True
                    queue.append(next_node)
        return cnt
    
    ans = n
    for v1, v2 in wires:
        cnt = bfs(v1, v2)
        ans = min(ans, abs((n - cnt) - cnt))
    return ans