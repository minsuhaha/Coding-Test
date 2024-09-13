import heapq
def solution(n, costs):
    graph = [[] for _ in range(n)]
    for n1, n2, cost in costs:
        graph[n1].append((n2, cost))
        graph[n2].append((n1, cost))
        
    heap = []
    visited = [False] * n
    visited[0] = True
    
    for n2, cost in graph[0]:
        heapq.heappush(heap, (cost, n2))
    
    total = 0
    while heap:
        cost, node = heapq.heappop(heap)
        
        if not visited[node]:
            visited[node] = True
            total += cost
            
            for next_node in graph[node]:
                heapq.heappush(heap, (next_node[1], next_node[0]))
    
    return total