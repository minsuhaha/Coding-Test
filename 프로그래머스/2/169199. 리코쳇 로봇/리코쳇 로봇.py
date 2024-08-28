from collections import deque
def solution(board):
    """
    D : 장애물 위치 / G : 목표지점 / . : 빈 공간 / R : 로봇 처음 위치
    로봇(R)이 목표지점(G)까지 최소거리로 도착해야 함
    """
    
    def bfs(x, y, move):
        queue = deque([(x, y, move)])
        visited[x][y] = True
        
        while queue:
            x, y, move = queue.popleft()
            
            if board[x][y] == 'G':
                return move
            
            for i in range(4):
                nx, ny = x, y
                
                while True:
                    nx += dx[i]
                    ny += dy[i]
                
                    if (nx<0 or nx>N-1 or ny<0 or ny >M-1) or board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                        
                if not visited[nx][ny]:
                    queue.append((nx, ny, move+1))
                    visited[nx][ny] = True
        return -1            

    
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    N, M = len(board), len(board[0])
    visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                return bfs(i, j, 0)