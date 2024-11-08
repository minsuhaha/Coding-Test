def solution(dirs):
    graph = [[] for _ in range(11)]
    for i in range(11):
        for j in range(11):
            graph[i].append((i, j))
    
    move = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    def bfs(x, y):
        for d in dirs:
            nx = x + move[d][0]
            ny = y + move[d][1]
            
            if 0<=nx<11 and 0<=ny<11:
                if ((x, y), (nx, ny)) not in visited and ((nx, ny),(x, y)) not in visited:
                    visited.add(((x, y),(nx, ny)))
                x, y = nx, ny
            
        return len(visited)
    
    visited = set()
    return bfs(5, 5)