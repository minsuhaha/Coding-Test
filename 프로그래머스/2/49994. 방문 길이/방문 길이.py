from collections import deque
def solution(dirs):
    visited = set()
    cnt = 0
    x, y = 5, 5

    for d in dirs:
        nx, ny = x, y
        if d == 'U':
            nx -= 1
        elif d == 'D':
            nx += 1
        elif d == 'R':
            ny += 1
        elif d == 'L':
            ny -= 1

        if nx < 0 or nx >= 11 or ny < 0 or ny >= 11:
            nx, ny = x, y
            continue
            
        if ((x,y,nx,ny)) not in visited and ((nx,ny,x,y)) not in visited:
            visited.add((x,y,nx,ny))
            cnt += 1
        x, y = nx, ny
    return cnt