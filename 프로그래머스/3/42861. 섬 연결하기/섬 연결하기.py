import heapq
def solution(n, costs):
    graph = [[] for _ in range(n)]
    for v1, v2, c in costs:
        graph[v1].append((v2, c))
        graph[v2].append((v1, c))
        
    
    def dijkstra(node):
        q = []
        heapq.heappush(q, (0, node))
        total_cost = 0
        node_cnt = 0
        
        while q:
            cost, node = heapq.heappop(q)
            
            if visited[node]:
                continue
            
            visited[node] = True
            total_cost += cost
            
            node_cnt += 1
            if node_cnt == n:
                return total_cost
            
            for next_node, next_cost in graph[node]:
                if not visited[next_node]:
                    heapq.heappush(q, (next_cost, next_node))
        
    visited = [False] * n
    return dijkstra(0)
        
        