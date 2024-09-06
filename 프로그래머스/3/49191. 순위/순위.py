from collections import deque, Counter
def solution(n, results):
    graph_win = [[] for _ in range(n+1)]
    graph_lose = [[] for _ in range(n+1)]
    
    for win_player, lose_player in results:
        graph_win[win_player].append(lose_player)
        graph_lose[lose_player].append(win_player)
    
    def bfs(graph, x):
        queue = deque([x])
        visited = [False]*(n+1)
        visited[x] = True
        cnt = 0
        
        while queue:
            node = queue.popleft()
            
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append((next_node))
                    cnt += 1
        return cnt
    
    answer = 0
    for i in range(1, n+1):
        if bfs(graph_win, i) + bfs(graph_lose, i) == n-1:
            answer += 1
    
    return answer
    