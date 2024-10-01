def solution(n):
    board = [[0]*n for _ in range(n)]
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오, 아래, 왼, 위
    
    total = n*n
    now = 0
    row, col = 0, -1
    idx = 0
    
    while now < total:
        next_row = row + move[idx][0]
        next_col = col + move[idx][1]
        
        if 0<=next_row<n and 0<=next_col<n and board[next_row][next_col] == 0:
            now += 1
            board[next_row][next_col] = now
            row, col = next_row, next_col
        else:
            idx = (idx+1) % 4 # 방향 꺽어주기
    
    return board
            