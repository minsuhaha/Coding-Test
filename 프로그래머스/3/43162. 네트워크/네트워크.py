from collections import deque
def solution(n, computers):
    answer = 0
    def bfs(node):
        queue = deque([node])
        visited[node] = True # 방문처리
        
        while queue:
            node = queue.popleft()
            
            for i in range(len(computers[node])):
                if computers[node][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    
    
    visited = [False] * n
    for i in range(n):
        if not visited[i]: # 아직 방문되지 않았다면
            bfs(i)
            answer += 1
            
    return answer