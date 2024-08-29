from collections import deque
def solution(maps):
    
    n, m = len(maps), len(maps[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False]*m for _ in range(n)]
    def bfs(x, y, z):
        queue = deque([(x,y,z)])
        visited[x][y] = True
        
        while queue:
            x, y, z = queue.popleft()
            
            if x == n-1 and y == m-1:
                return z
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<n and 0<=ny<m:
                    if maps[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx,ny,z+1))
        return -1
    
    return bfs(0,0,1)