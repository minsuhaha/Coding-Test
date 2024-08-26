from collections import deque
def solution(maps):
    result = []
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        cnt = int(maps[x][y])
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                    if maps[nx][ny] != 'X' and not visited[nx][ny]:
                        cnt += int(maps[nx][ny])
                        queue.append((nx, ny))
                        visited[nx][ny] = True
        return cnt
            
    
    visited = [[False]*len(maps[i]) for i in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X' and not visited[i][j]:
                result.append(bfs(i, j))
    
    if result:
        result.sort()
        return result
    else:
        return [-1]