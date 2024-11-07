from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = 1
        
        while queue:
            x, y = queue.popleft()
            
            if x == n-1 and y == m-1:
                return visited[x][y]
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                
                if 0<=nx<n and 0<=ny<m:
                    if not visited[nx][ny] and maps[nx][ny] == 1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
        return -1
    
    visited = [[0]*m for _ in range(n)]
    return bfs(0, 0)