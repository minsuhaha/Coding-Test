'''
1. 레버가 있는 칸으로 이동 : 'S' -> 'L'
2. 문을 찾아서 이동 : 'L' -> 'E'
해당 과정에서 이동거리 최소 값 구하기
'''
from collections import deque
def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs_start(x, y):
        queue = deque([(x, y)])
        visited = [[0]*len(maps[i]) for i in range(len(maps))]
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                    if maps[nx][ny] == 'L':
                        return visited[x][y] + 1
                    if (maps[nx][ny] == 'O' or maps[nx][ny] == 'E') and not visited[nx][ny]: 
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
        return -1
        
    def bfs_end(x, y):
        queue = deque([(x, y)])
        visited = [[0]*len(maps[i]) for i in range(len(maps))]
        
        while queue:
            x, y = queue.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                    if maps[nx][ny] == 'E':
                        return visited[x][y] + 1
                    if (maps[nx][ny] == 'O' or maps[nx][ny] == 'S') and not visited[nx][ny]: 
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))
        return -1
    
    s_x, s_y, l_x, l_y = 0, 0, 0, 0 
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                s_x, s_y = i, j
            elif maps[i][j] == 'L':
                l_x, l_y = i, j
    
    
    cnt1 = bfs_start(s_x, s_y)
    cnt2 = bfs_end(l_x, l_y)
    
    if cnt1 == -1 or cnt2 == -1:
        return -1
    return cnt1 + cnt2
                
    
    
    